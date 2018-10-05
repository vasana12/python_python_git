import sqlite3

dbconn = sqlite3.connect('tel.db')

dbcursor = dbconn.cursor()
dbcursor.execute("drop table if exists tel")
dbcursor.execute("create table if not exists tel\
                 (id integer primary key autoincrement, name text, tel text, \
                 addr text, input_time text, memo text)")
# Unlike DDL, DML(Data Manipulateion Language) commands need to be commited/rolled back.

dbcursor.close()
dbconn.close()

#1. connect(db이름) 메소드로 연결할 db설정, 연결된 Connection 객체를 dbconn 에 담는다
#2. 연결객체로 커서 객체를 생성한다
#3. 연결객체로 커리를 실행한다.
#4. cursor 객체와 Connection 객체를 닫는다