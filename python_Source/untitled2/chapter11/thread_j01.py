#-*-coding: utf-8 -*-
#threading.Thread 의 생성자로 호출할 객체를 전달하는 방법

import threading

def Mythread():
    for i in range(5):
        print(i)
#실행하는 코드 작성후
if __name__=='__main__':
    t = threading.Thread(target=Mythread) # Mythread를 스레드로 생성한다.
    t.start() #Thread(target=Mythread)의 target로 전달해서 함수를 실행 시킨다.

