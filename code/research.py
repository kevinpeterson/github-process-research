import requests
import json
import time
import os
import urllib2
import random

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String, DateTime

from config import *
 
engine = create_engine('mysql://'+db_username+'@'+db_host+':'+str(db_port)+'/'+db_database, echo=False)
 
metadata = MetaData(bind=engine)
 
repository_table = Table('repository', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(60)),
                    Column('forks', Integer),
                    Column('open_issues', Integer),
                    Column('watchers', Integer),
                    mysql_engine='InnoDB',
                    )

issue_table = Table('issue', metadata,
					Column('id', Integer, autoincrement=True, primary_key=True),
                    Column('repository_id', Integer, ForeignKey('repository.id')),
                    Column('creator', String(60)),
                    Column('name', String(60)),
                    Column('number', Integer),
                    Column('open_date', DateTime),
                    Column('close_date', DateTime),
                    mysql_engine='InnoDB',
                    )

commit_table = Table('commit', metadata,
					Column('id', Integer, autoincrement=True, primary_key=True),
                    Column('repository_id', Integer, ForeignKey('repository.id')),
                    Column('committer', String(60)),
                    mysql_engine='InnoDB'
                    )
 
 
# create tables in database
metadata.create_all()

session = requests.Session()
session.auth = (github_username, github_password)

response = urllib2.urlopen('https://raw.github.com/gist/4669395')
random_words = response.readlines()

def _get_random_repo():
	repo_json = None
	while True:
		keyword = random.choice(random_words)
		response = session.get('https://api.github.com/legacy/repos/search/'+keyword)
		_check_quota(response)
		if(response.ok):
			repos = json.loads(response.text or response.content)
			if(len(repos['repositories']) > 0):
				repo = random.choice(repos['repositories'])
				response = session.get('https://api.github.com/repos/'+repo['username']+'/'+repo['name'])
				if(response.ok):
					return json.loads(response.text or response.content)

def _check_quota(response):
	requests_left = int(response.headers['X-RateLimit-Remaining'])
	if(requests_left == 0):
		print "Sleeping for 65 minutes... Good Night."
		time.sleep(65 * 60)
	print requests_left

def crawl(sample_size):
	while(sample_size > 0):
		try:
			repo = _get_random_repo();
			i = repository_table.insert([repo])
			i.execute()
			url = 'https://api.github.com/repos/'+repo['full_name']+'/commits?per_page=100'
			while url is not None:
				response = session.get(url)
				_check_quota(response)
				if(response.ok):
					commits = json.loads(response.text or response.content)
					for commit in commits:
						committer = None
						if 'author' in commit and commit['author'] is not None:
							committer = commit['author']['login']
						else:
							committer = commit['commit']['author']['name'].encode('unicode_escape')
						 
						i = commit_table.insert(
							dict(
								repository_id=repo['id'],
								committer=committer))
						i.execute()
					links = response.links
					if 'next' in links:
						url = response.links["next"]['url']
					else:
						url = None
				else:
					url = None

			for tag in ['closed', 'open']:
				url = 'https://api.github.com/repos/'+repo['full_name']+'/issues?per_page=100&state='+tag
				while url is not None:
					response = session.get(url)
					_check_quota(response)
					if(response.ok):
						issues = json.loads(response.text or response.content)
						for issue in issues:
							i = issue_table.insert(
								dict(
									number=issue['number'],
									repository_id=repo['id'],
									creator=issue['user']['login'],
									open_date=issue['created_at'],
									close_date=issue['closed_at']))
							i.execute()
						links = response.links
						if 'next' in links:
							url = response.links["next"]['url']
						else:
							url = None
					else:
						url = None

			sample_size -= 1

		except Exception as e:
			print e


crawl(999)
