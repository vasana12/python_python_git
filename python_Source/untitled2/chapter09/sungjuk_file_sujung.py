from sungjuk_class_not_GetSet_TT import Sungjuk
import pickle,os

students=[]

def f_menu():
    print("***메뉴***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")

def f_input():
    fp = open("binary.dat", "wb")
    while True:
        obj = Sungjuk()
        if obj.input_sungjuk():
            break
        obj.process_sungjuk()
        pickle.dump(obj,fp)
        print()

def f_output():
    total_avg =0
    fp = open("binary.dat", "rb")
    while True:
        if (fp.tell() == os.fstat(fp.fileno()).st_size):
            break
        obj = pickle.load(fp)
        if len(students)==0:
            students.append(obj)
        else:
            for data in students:
                if data._hakbun==obj._hakbun:
                    pass
                else:
                    students.append(obj)
                    print("cc")
        s = "성적표"
        print(s.center(47, "*"))
        print("=" * 50)
        print("\n학번     이름   국어   영어   수학   총점   평균   등급")
        print("=" * 50)
        for obj in students:
            total_avg += obj._avg
            obj.output_sungjuk()
        print("=" * 50)
        print("         총학생수 = %d, 전체 평균= %.2f\n" % (len(students), total_avg / len(students)))
    fp.close()
def f_search():
    fp = open("binary.dat", "rb")
    while True:
        if (fp.tell() == os.fstat(fp.fileno()).st_size):
            break
        obj = pickle.load(fp)
        if len(students)==0:
            students.append(obj)
        else:
            for data in students:
                if data._hakbun==obj._hakbun:
                    pass
                else:
                    students.append(obj)
    hakbun = input("\n 조회할 학번을 입력하세요:")
    for obj in students:
        if(obj._hakbun == hakbun):
            print("\n학번     이름   국어   영어   수학   총점   평균   등급")
            print("=" * 50)
            obj.output_sungjuk()
            print("=" * 50)
            break
        else:
            print("\n조회할 학번%s가 없습니다!!\n"%hakbun)

def f_update():
    fp = open("binary.dat", "rb")
    while True:
        if (fp.tell() == os.fstat(fp.fileno()).st_size):
            break
        obj = pickle.load(fp)
        if len(students)==0:
            students.append(obj)
        else:
            for data in students:
                if data._hakbun==obj._hakbun:
                    pass
                else:
                    students.append(obj)
    hakbun = input("\n수정할 학번을 입력하세요:")
    for obj in students:
        if (obj._hakbun==hakbun):
            obj._kor = int(input("국어점수를입력하세요"))
            obj._eng = int(input("영어점수"))
            obj._math = int(input("수학점수를 입력하세요"))
            obj.process_sungjuk()
            print("\n학번 %s 성적정보 수정 성공!!\n" %obj._hakbun)
            break
        else:
            print("\n수정할 제품코드 %s가 없습니다!!\n" %obj._hakbun)
def f_delete():
    fp = open("binary.dat", "rb")
    while True:
        if (fp.tell() == os.fstat(fp.fileno()).st_size):
            break
        obj = pickle.load(fp)
        if len(students)==0:
            students.append(obj)
        else:
            for data in students:
                if data._hakbun==obj._hakbun:
                    pass
                else:
                    students.append(obj)
    hakbun =input("\n삭제할 학번을 입력하세요:")
    for obj in students:
        if (obj._hakbun ==hakbun):
            students.remove(obj)
            print("\n학번 %s 성적정보 삭제 성공!!\n"%obj._hakbun)
            break
    else:
        print("\n삭제할 제품코드 %s가 없습니다!!\n"%hakbun)

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


# test=Sungjuk()
# lst = []
# def call_menu():
#     while True:
#         s = " 메뉴 "
#         print(s.center(10, "*"))
#         print("1.성적정보 입력")
#         print("2.성적정보 출력")
#         print("3.성적정보 조회")
#         print("4.성적정보 수정")
#         print("5.성적정보 삭제")
#         print("6.프로그램 종료")
#         a=int(input("메뉴를 선택하세요(1~6) :"))
#         if a==1:
#             test.input_sungjuk(lst)
#         elif a==2:
#             print(s.center(47, "*"))
#             print("=" * 50)
#             print("학번     이름   국어   영어   수학   총점   평균   등급")
#             print("=" * 50)
#             test.output_sungjuk(lst)
#             print("=" * 50)
#         elif a==3:
#             print(s.center(47, "*"))
#             print("=" * 50)
#             print("학번     이름   국어   영어   수학   총점   평균   등급")
#             print("=" * 50)
#             test.select_sungjuk(lst)
#             print("=" * 50)
#         elif a==4:
#             test.update_sungjuk(lst)
#         elif a==5:
#             test.delete_sungjuk(lst)
#         else :
#             break
#
# if __name__=='__main__':
#     call_menu()
