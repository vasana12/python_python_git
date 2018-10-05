#-*-coding:utf8 -*-

def Hello(): #리턴값이 없는 함수
    print('hello')

def Hello02(): #리턴값이 있는 함수
    return 'hi'
if __name__ == "__main__": #프로그램 실행의 진입점
    print(Hello())
    print(Hello02())