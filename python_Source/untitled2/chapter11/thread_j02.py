#-*-coding: utf-8 -*-
#threading.Thread 서브클래스를 만들고 run() 메소드를 오버라이딩 하는 방법

import threading

class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        for i in range(5):
            print(self.name,":",i)
if __name__=="__main__":
    t1= MyThread("멍멍이")
    t2= MyThread("야옹이")
    t1.start()
    t2.start()
