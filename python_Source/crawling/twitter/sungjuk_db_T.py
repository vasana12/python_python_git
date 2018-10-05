#-*-coding:utf-8-*-
import sqlite3
from chapter12.sungjuk_class_db import Sungjuk

def create_table():
    dbconn = sqlite3.connect('sungjuk.db')

    dbcursor = dbconn.cursor()
    dbcursor.execute("""create table if not exists sungjuk(
        hakbun text primary key,
        irum text,
        kor integer,
        eng integer,
        math integer,
        tot integer,
        avg real,
        grade text)""")
    dbcursor.close()
    dbconn.close()

def f_menu():
    print("***메뉴***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")

def f_input():
    obj = Sungjuk()
    print()
    obj.input_sungjuk()
    obj.process_sungjuk()

    sql = "insert into sungjuk (hakbun, irum, kor, eng, math, tot, avg, \
            grade)values(?,?,?,?,?,?,?,?)"
    dbconn = sqlite3.connect('sungjuk.db') #데이터베이스 연결
    dbcursor = dbconn.cursor()
    dbcursor.execute(sql, (str(obj.hakbun),str(obj.irum),obj.kor,
                           obj.eng, obj.math, obj.tot, obj.avg,str(obj.grade)))
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

    print("\n성적정보 입력 성공!!\n")

def f_output():
    total_avg=0

    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()

    dbcursor.execute("SELECT count(*) FROM sungjuk")
    cnt = dbcursor.fetchone()[0] # fechone() : 한개의 레코드 (튜플형식)
    res = dbcursor.execute("SELECT*FROM sungjuk order by hakbun asc")

    #dbcursor.execute ( 'SELECT * FROM sungjuk order by hakbun asc')
    #res = dbcursor.fetchall() # fetchall() : 모든 레코드. 튜플형식을 리스트에 추가한 형식으로 반환

    print("\n                   ***성적표***")
    print("================================================")
    print("학번   이름   국어   영어   수학   총점    평균   등급")
    print("================================================")
    for row in res: #
        total_avg+=row[6]
        print("%4s  %4s  %3d   %3d    %3d    %3d    %6.2f    %s"
              %(row[0],row[1],int(row[2]),int(row[3]),int(row[4]),int(row[5]),float(row[6]),row[7]))
    print("================================================")
    print("               총학생수 = %d, 전체평균 = %.2f\n" %(cnt,total_avg/cnt))
    dbcursor.close()
    dbconn.close()

def f_search():
    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()

    #res = dbcursor.execute("SELECT * FROM sungjuk order by habkun asc")
    hakbun = input("\n조회할 학번을 입력하세요:")
    res = dbcursor.execute("SELECT*FROM sungjuk where hakbun=?", (hakbun,))
    for row in res:
        if (row[0]==hakbun):
            print("학번   이름   국어   영어   수학   총점    평균   등급")
            print("=====================================================")
            print("%4s  %4s  %3d   %3d    %3d    %3d    %6.2f    %s"
                  % (row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), float(row[6]), row[7]))
            print("=====================================================")
            break
    else:
        print("\n조회할 학번%s가 없습니다!!\n" % hakbun)

    dbcursor.close()
    dbconn.close()

def f_update():
    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()

    hakbun = input("\n수정할 학번을 입력하세요:")
    res = dbcursor.execute("SELECT*FROM sungjuk where hakbun=?",(hakbun,))
    for row in res:
        if(row[0]==hakbun):
            obj = Sungjuk()
            obj.hakbun = row[0]
            obj.kor = int(input("국어점수를 입력하세요"))
            obj.eng = int(input("영어점수를 입력하세요"))
            obj.math = int(input("수학점수를 입력하세요"))
            obj.process_sungjuk()

            #sql = "update sungjuk set kor = " + str(obj.kor) + ", eng
            dbcursor.execute("update sungjuk set kor=?,eng=?,math=?, tot=?, avg=?,\
                grade=? where hakbun=?",\
                             (obj.kor,obj.eng,obj.math,obj.tot,obj.avg,obj.grade,obj.hakbun))
            print("\n학번 %s 성적정보 수정 성공 !!\n" %obj.hakbun)
            break
    else:
        print("\n수정할 제품코드 %s 가 없습니다!!\n"%hakbun)

    dbconn.commit()
    dbcursor.close()
    dbconn.close()

def f_delete():
    dbconn = sqlite3.connect("sungjuk.db")
    dbcursor = dbconn.cursor()

    #res = dbcursor.execute("SELECT*FROM sungjuk order by hakbun asc")

    hakbun = input("\n삭제할 학번을 입력하세요:")
    res = dbcursor.execute("SELECT* FROM sungjuk where hakbun=?",(hakbun,))
    for row in res:
        if row[0]==hakbun:
            dbcursor.execute("delete FROM sungjuk where hakbun=?",(hakbun,))
            print("\n학번 %s 성적정보 삭제 성공 !!\n" % hakbun)
            break
        else:
            print("\n삭제할 제품코드 %ss 가 없습니다!!\n" % hakbun)

        dbconn.commit()
        dbcursor.close()
        dbconn.close()

if __name__ =='__main__':
    create_table()
    while True:
        f_menu()
        menu =int(input("\n메뉴를 선택하세요:"))

        if menu==1 :
            f_input()
        elif menu==2:
            f_output()
        elif menu==3:
            f_search()
        elif menu==4:
            f_update()
        elif menu==5:
            f_delete()
        elif menu==6:
            break
        else:
            print("숫자(1~6) 다시 입력하세요")