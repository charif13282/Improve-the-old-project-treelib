import sqlite3
conn=sqlite3.connect('database.sqlite')
gon=conn.cursor()
res=gon.execute('select name from sqlite_master where type="table"')
res=gon.execute('select * from admins')
print(res.fetchall())
conn.commit()
conn.close()