#-*-coding:utf-8-*-
import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

name = input("삭제할 이름 입력:")
res= dbcursor.execute("delete from tel where name=?",(name,))

dbconn.commit()

dbcursor.close()
dbconn.close()