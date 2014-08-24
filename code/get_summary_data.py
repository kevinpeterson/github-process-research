##############################################################
# get_summary_data.py
#
# Builds the data summary table (Table 1: GitHub summary statistics).
#
# License: MIT 2014 Kevin Peterson
##############################################################
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

	# read in the main SQL analytics
	with open ("research.sql", "r") as sql_file:
		sql = sql_file.read()

	cur.execute(sql)

	desc = cur.description

	rows = cur.fetchall()

	col_processor = {
		0:lambda x: x,
		1:lambda x: round(x,2),
		2:lambda x: int(x),
		3:lambda x: int(x),
		4:lambda x: round(x,2)
	}

	# output the LaTeX table
	for row in rows:
		for i in range(0,5):
			print col_processor[i](row[i]),
			print ' \\\\' if i == 4 else ' & ',
		print

except Exception as e:
	print e

finally:
	con.close()
