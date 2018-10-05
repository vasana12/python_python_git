#-*-coding:utf-8-*-
import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

name = input("수정할 이름 입력:")
sql = "SELECT*FROM tel where name=?"
res = dbcursor.execute(sql,(name,))
flag = 0
for dd in res:
        tel =input("전화번호:")
        addr = input("주소:")
        memo = input("메모:")
        dbcursor.execute("update tel set tel=?, addr=?, memo=? where name=?",
                         (tel, addr, memo, name))
        dbconn.commit()
        flag=1

if flag ==0:
    print("\n수정 실패!!\n")
else:
    print("\n수정 성공!!\n")

dbcursor.close()
dbconn.close()
