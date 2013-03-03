import MySQLdb as mdb
from decimal import Decimal
from config import *

try:
	con = mdb.connect(
		host=db_host,
		user=db_username,
		passwd=db_password,
		db=db_database,
		port=db_port)

	cur = con.cursor()

	with open ("research.sql", "r") as sql_file:
		sql = sql_file.read()

	cur.execute(sql)

	desc = cur.description

	rows = cur.fetchall()

	for row in rows:
		for i in range(0,5):
			print row[i],
			print ' \\\\' if i == 4 else ' & ',
		print

except Exception as e:
	print e

finally:
	con.close()
