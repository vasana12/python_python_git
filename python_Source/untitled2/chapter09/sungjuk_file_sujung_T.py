from sungjuk_class_T import Sungjuk
import pickle,os

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
    fp = open("sungjuk.dat", "ab")
    print()

    obj.input_sungjuk()
    obj.process_sungjuk()

    pickle.dump(obj, fp)
    fp.close()
    print("\n성적정보 입력 성공!! \n")

def f_output():
    total_avg =0
    cnt = 0
    students=[]

    if not os.path.isfile(file_path):
        print("\n출력할 데이터가 없습니다. \n")
        return


    fp = open("sungjuk.dat", "rb")

    if os.fstat(fp.fileno()).st_size == 0: # 파일 용량이 0인지 검사
        print("\n출력할 데이터가 없습니다. \n")
        return

    s = "성적표"
    print(s.center(47, "*"))
    print("=" * 50)
    print("\n학번     이름   국어   영어   수학   총점   평균   등급")
    print("=" * 50)

    while True:
        obj = pickle.load(fp)
        total_avg += obj.avg #obj.avg 대신 obj.get_avg() 도 가능
        obj.output_sungjuk()
        cnt+=1
        if(fp.tell()==os.fstat(fp.fileno()).st_size):
            break
    fp.close()
    print("=" * 50)
    print("         총학생수 = %d, 전체 평균= %.2f\n" % (cnt, total_avg / cnt))

def f_search():

    if not os.path.isfile(file_path):
        print("\n조회할 데이터가 없습니다. \n")
        return

    fp = open("sungjuk.dat", "rb")

    if os.fstat(fp.fileno()).st_size == 0: #파일 용량이 0인지 검사
        print("\n조회할 데이터가 없습니다. \n")
        return


    hakbun = input("\n 조회할 학번을 입력하세요:")
    flag = 0

    while True:
        obj = pickle.load(fp)
        if obj.hakbun ==hakbun:
            print("\n학번     이름   국어   영어   수학   총점   평균   등급")
            print("=" * 50)
            obj.output_sungjuk()
            flag = 1
            print("=" * 50)
            break
        if (fp.tell() == os.fstat(fp.fileno()).st_size):
            break

    if (flag == 0):
        print("\n조회할 학번 %s가 없습니다. " % hakbun)


def f_update():

    if not os.path.isfile(file_path):  # file path 에 해당하는 파일이 있는지 검사
        print("\n출력할 데이터가 없습니다!!!\n")
        return

    fp = open("sungjuk.dat", "rb")

    if os.fstat(fp.fileno()).st_size == 0:  # 파일 용량이 0인지 검사
        print("\출력할 데이터가 없습니다!!!\n")
        return

    hakbun = input("\n수정할 학번을 입력하세요:")
    flag=0
    students = []
    while True:
        obj = pickle.load(fp)
        students.append(obj)
        if (obj._hakbun==hakbun):
            obj._kor = int(input("국어점수를입력하세요"))
            obj._eng = int(input("영어점수"))
            obj._math = int(input("수학점수를 입력하세요"))
            obj.process_sungjuk()
            print("\n학번 %s 성적정보 수정 성공!!\n" %obj._hakbun)
            flag=1

        if (fp.tell()==os.fstat(fp.fileno()).st_size):
            break

    fp.close()

    if flag==1: #데이터에 변화가 발생한 경우에만 패일로 새로 출력한다.
        fp = open("sungjuk.dat","wb") #수정한 데이터를 다시 파일에 저장하기 위헤 wb 모드로 오픈.
        for obj in students: #리스트에 저장한 데이터를 다시 파일에 저장.
            pickle.dump(obj,fp)
        fp.close()
    if (flag==0):
        print('\수정할 학번 %s 가 없습니다!!')

def f_delete():
    if not os.path.isfile(file_path):  # file path 에 해당하는 파일이 있는지 검사
        print("\n출력할 데이터가 없습니다!!!\n")
        return;

    fp = open("sungjuk.dat", "rb")

    if os.fstat(fp.fileno()).st_size == 0:  # 파일 용량이 0인지 검사
        print("\출력할 데이터가 없습니다!!!\n")
        return

    hakbun = input("\n삭제할 학번을 입력하세요:")

    flag=0
    students= []
    while True:
        obj = pickle.load(fp)
        students.append(obj)
        if obj.hakbun == hakbun:
            students.remove(obj)
            print("\n학번%s 성적정보 삭제 성공!!\n" %obj.hakbun)
            flag=1
        if (fp.tell()==os.fstat(fp.fileno()).st_size):
            break
    fp.close()

    if flag==1: #데이터에 변화가 발생한 경우에만 파일로 새로 출력한다.
        fp=open("sungjuk.dat", "wb") #삭제한 데이터를 다시 파일에 저장하기 위해 wb 모드로 오픈.
        for obj in students: #리스트에 저장한 데이터를 다시 파일에 저장.
            pickle.dump(obj,fp)

        fp.close()
    if flag == 0:
        print("\n삭제할 학번 %s 가 없습니다!!!\n"%hakbun)

if __name__=="__main__":
    file_path = os.getcwd() + "\sungjuk.dat" # 성적 데이터 파일 경로와 파일명 설정

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



