import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', passwd='root')
if con.is_connected():
  print('Connection Established')
else:
  print('Connection Error')
cursor = con.cursor()
cursor.execute(a)
con.close()
