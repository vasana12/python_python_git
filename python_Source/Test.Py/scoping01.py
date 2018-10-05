x=50
def func():
    #global x    #함수 밖에 선언된 전역변수를 참조한다. 주석처리하면 에러가 남
    print('x is', x)
    #x=2    #지역변수 주석처리하면 전역변수를 참조한다. 지역변수 없으면 전역변수 전역변수 없으면 built in에서 찾는다.
    print('Change global x to', x)

if __name__=='__main__':
    print(func())      #return 값이 없어서 none 이 나옴
    print(x)