#-*-coding: utf-8 -*-
import threading
import time

def Mythread():
    for i in range(10):
        print("Mythread =", i)
        time.sleep(0.5)
if __name__=='__main__':
    t=threading.Thread(target=Mythread)
    t.start()
    for i in range(10):
        print("main=", i)
        time.sleep(0.5)
