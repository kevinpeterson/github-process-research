import sys
import MySQLdb
from config import *
from pylab import *
from matplotlib import rc		
import matplotlib.pyplot as plt
import numpy

class PieChart:
	def __init__(self, sql):
		self.sql = sql

	def plot(self, filename):
		db = MySQLdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_database)
		cursor = db.cursor()

		cursor.execute(self.sql)

		result = cursor.fetchall()

		ranges = {'0-5':0,'5-10':0,'10-50':0,'50-95':0,'95-100':0}

		for record in result:
			percentage = record[0]
			if 0 <= percentage < 5:
				ranges['0-5'] += 1
			elif 5 <= percentage < 10:
				ranges['5-10'] += 1
			elif 10 <= percentage < 50:
				ranges['10-50'] += 1
			elif 50 <= percentage < 95:
				ranges['50-95'] += 1
			elif 95 <= percentage <= 100:
				ranges['95-100'] += 1

		fig = plt.figure()

		plt.pie(ranges.values(), labels=[key + "%" for key in sorted(ranges.keys(), key=lambda key: int(key.split('-')[0]))], autopct=None, shadow=True)

		plt.legend(title="Contribution")

		F = gcf()
		F.savefig("../paper/images/"+filename+".png")
		plt.close(fig)

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

		plt.scatter(x,y)

		correlation_coefficient = "%.4f" % numpy.corrcoef(x,y)[0,1]
		title('Correlation Coefficient: ' + correlation_coefficient)

		if float(correlation_coefficient) > 0.5:
			plt.plot(x,y,'bo',x,m*numpy.array(x)+b,'-k',linewidth=2)

		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)
		plt.xlim(self.xrange)
		plt.ylim(self.yrange)
	
		F = gcf()
		F.savefig("../paper/images/"+filename+".png")
		plt.close(fig)

		f = open("../paper/"+filename+"-correlation.tex",'w')
		f.write(str(correlation_coefficient))
		f.close()

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