import MySQLdb as mdb

try:
	con = mdb.connect('localhost', 'root', '')

	cur = con.cursor()

	with open ("research.sql", "r") as sql_file:
		sql = sql_file.read()

	cur.execute(sql)

	desc = cur.description

	rows = cur.fetchall()

	for row in rows:
		print row[0]

finally:
	con.close()
