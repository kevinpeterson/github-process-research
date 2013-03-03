import sys
import MySQLdb
from config import *
from pylab import *
from matplotlib import rc

class Histograph:
	def __init__(self, sql, xlabel, ylabel, range=None):
		self.sql = sql
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.range = range

	def plot(self, filename):
		db = MySQLdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_database)
		cursor = db.cursor()

		cursor.execute(self.sql)

		result = cursor.fetchall()

		y = []

		for record in result:
		  y.append(record[0])

		import matplotlib.pyplot as plt

		plt.hist(y, range=self.range)
		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)

		F = gcf()
		F.savefig("../paper/images/"+filename+".png")
		plt.close()