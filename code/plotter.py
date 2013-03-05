import sys
import MySQLdb
from config import *
from pylab import *
from matplotlib import rc		
import matplotlib.pyplot as plt
import numpy

class ScatterPlot:
	def __init__(self, sql, xlabel, ylabel, xrange=None, yrange=None):
		self.sql = sql
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.xrange = xrange
		self.yrange = yrange

	def plot(self, filename):
		db = MySQLdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_database)
		cursor = db.cursor()

		cursor.execute(self.sql)

		result = cursor.fetchall()

		x = []
		y = []

		for record in result:
			x.append(record[0])
			y.append(record[1])

		fig = plt.figure() 
		m,b = numpy.polyfit(x,y,1)
		print("Slope: %s, B: %s") % (m,b)

		plt.plot(x,y,'bo',x,m*numpy.array(x)+b,'-k',linewidth=2)

		plt.scatter(x,y)

		correlation_coefficient = numpy.corrcoef(x,y)[0,1]
		title('Correlation Coefficient: ' + str(correlation_coefficient))

		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)
		plt.xlim(self.xrange)
		plt.ylim(self.yrange)
	
		F = gcf()
		F.savefig("../paper/images/"+filename+".png")
		plt.close(fig)

		return correlation_coefficient

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

		x = []

		for record in result:
		  x.append(record[0])

		fig = plt.figure() 
		plt.hist(x, range=self.range)
		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)

		F = gcf()
		F.savefig("../paper/images/"+filename+".png")
		plt.close(fig)