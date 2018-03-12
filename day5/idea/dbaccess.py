#import cx_Oracle as db
#import cx_Oracle
#conn = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
import sqlite3 as db
conn = db.connect('users.db')
curr = conn.cursor()
# To create table
table = '''
CREATE TABLE `user` (
	`name`	TEXT,
	`sal`	REAL
)
'''
#curr.execute(table)
# To insert into the database
#ins = 'insert into user values("Aditya",100000 )'
#curr.execute(ins)
#conn.commit()

# Execute many
# ins = [["Arun", 2000],["John", 200],["Jane", 5000000]]
# ins_query = 'insert into user values(?,?)'
# curr.executemany(ins_query, ins)
# conn.commit()

# query data using fetchall
sql_q = 'select * from user'
curr.execute(sql_q)
data = curr.fetchall()
data = [ "<tr><td>"+ row[0] + '</td><td>' + str(row[1]) + "</td></tr>" for row in data]
print data
content = "<table border=1>" + "<br>".join(data) + '</table>'
print content
import genhtml
genhtml.report({'heading': "Empolyee Report", 'content': content, 'tableheader':"Salary Report"})
curr.close()
conn.close()