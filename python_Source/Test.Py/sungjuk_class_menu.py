from sungjuk_class_list import Sungjuk

test=Sungjuk()
lst = []
def call_menu():
    while True:
        s = " 메뉴 "
        print(s.center(10, "*"))
        print("1.성적정보 입력")
        print("2.성적정보 출력")
        print("3.성적정보 조회")
        print("4.성적정보 수정")
        print("5.성적정보 삭제")
        print("6.프로그램 종료")
        a=int(input("메뉴를 선택하세요(1~6) :"))
        if a==1:
            test.input_sungjuk(lst)
        elif a==2:
            print(s.center(47, "*"))
            print("=" * 50)
            print("학번     이름   국어   영어   수학   총점   평균   등급")
            print("=" * 50)
            test.output_sungjuk(lst)
            print("=" * 50)
        elif a==3:
            print(s.center(47, "*"))
            print("=" * 50)
            print("학번     이름   국어   영어   수학   총점   평균   등급")
            print("=" * 50)
            test.select_sungjuk(lst)
            print("=" * 50)
        elif a==4:
            test.update_sungjuk(lst)
        elif a==5:
            test.delete_sungjuk(lst)
        else :
            break

if __name__=='__main__':
    call_menu()
