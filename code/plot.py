import sys
import matplotlib.pyplot as plt
import MySQLdb


db = MySQLdb.connect(host="localhost", user="root", passwd="", db="github")
cursor = db.cursor()

query = '''
select forks, count(*) FROM github.repository r inner join github.commit c on r.id = c.repository_id group by repository_id
'''
cursor.execute(query)

result = cursor.fetchall()

t = []
s = []

for record in result:
  t.append(record[0])
  s.append(record[1])

plt.plot(t, s, 'ko')
plt.ylim(0,3000)
plt.xlim(0,400)
plt.title("Forks V Commits")
plt.xlabel("Forks",fontsize=12)
plt.ylabel("Commits",fontsize=12)
plt.show()
#F = gcf()
#DPI = F.get_dpi()
#F.savefig('plot.png',dpi = (80))