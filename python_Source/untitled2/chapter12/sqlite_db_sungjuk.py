#-*-coding:utf-8-*-
import sqlite3
from chapter12.sungjuk_class_db import Sungjuk
dbconn = sqlite3.connect('tel.db')

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

    dbcursor.execute("insert into sungjuk(hakbun , irum , kor , eng , math, tot, avg, grade)\
     values('" + obj.hakbun + "', '" + obj.irum + "','" + str(obj.kor) + "','" + str(obj.eng) + "','" + str(
        obj.math) + "','"+str(obj.tot)+"','"+str(obj.avg)+"','"+str(obj.grade)+"')")
    dbconn.commit()
    print("\n성적정보 입력 성공!! \n")

def f_output():

    obj= Sungjuk()
    s = "성적표"
    print(s.center(47, "*"))
    print("=" * 50)
    print("\n학번     이름   국어   영어   수학   총점   평균   등급")
    print("=" * 50)
    obj.output_sungjuk()

def f_search():
    hakbun = input("조회할 학번을 입력하세요:")
    dbcursor.execute("SELECT*FROM sungjuk where hakbun=?",
                     (hakbun,))
    lst = dbcursor.fetchall()
    print("\n학번     이름   국어   영어   수학   총점   평균   등급")
    print("-" * 50)
    for row in lst:
        print("%4s    %3s   %3d   %3d    %3d    %3d   %6.2f   %s" %
              (str(row[0]), str(row[1]), row[2], row[3],
               row[4], row[5], row[6], row[7]))
    print("-" * 50)
    dbcursor.close()
    dbconn.close()

def f_update():
    obj=Sungjuk()

    obj.hakbun = input("\n수정할 학번을 입력하세요:")
    res=dbcursor.execute("SELECT*FROM sungjuk where hakbun=?",
                     (obj.hakbun,))
    flag=0
    for row in res:
        obj.kor = int(input("국어점수를입력하세요"))
        obj.eng = int(input("영어점수"))
        obj.math = int(input("수학점수를 입력하세요"))
        obj.process_sungjuk()
        print("\n학번 %s 성적정보 수정 성공!!\n" %obj.hakbun)
        dbcursor.execute("update sungjuk set kor=?, eng=?, math=?, tot=?, avg=? ,grade=? where hakbun=?",
                         (obj.kor, obj.eng, obj.math, obj.tot, obj.avg, obj.grade, obj.hakbun))
        dbconn.commit()
        flag=1
    if flag == 0:
        print("\n수정 실패!!\n")
    else:
        print("\n수정 성공!!\n")
def f_delete():
    hakbun = input("삭제할 학번 입력:")
    res = dbcursor.execute("delete from sungjuk where hakbun=?", (hakbun,))
    print("\n학번 %s 성적정보 삭제 성공!!\n" % hakbun)
    dbconn.commit()
    dbcursor.close()
    dbconn.close()


if __name__=="__main__":
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