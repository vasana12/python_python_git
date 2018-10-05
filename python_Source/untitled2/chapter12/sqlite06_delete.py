#-*-coding:utf-8-*-
import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res= dbcursor.execute('SELECT*FROM tel order by id desc')


name = input("삭제할 이름 입력:")

dbcursor.execute('delete from tel where name=?',(name,))
flag = 0

for row in res:
    if row[1]== name:
        dbcursor.execute("delete from tel where name=?",(name,))
        dbconn.commit()
        flag=1
if flag ==0:
    print("삭제 실패!!")
else:
    print("삭제 성공!!")

dbcursor.close()
dbconn.close()