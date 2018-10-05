#-*-coding: utf-8 -*-
import threading
import time

class MyThread(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name + ':'+str(i))
            time.sleep(0.5)

if __name__=='__main__':
    t1 = MyThread("야옹이")
    t2 = MyThread("멍멍이")
    t1.start()
    t2.start()