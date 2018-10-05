#-*-coding: utf-8 -*-
import threading
import time
def Mythread():
    for i in range(100):
        print(i)
if __name__=='__main__':
    t = threading.Thread(target=Mythread)
    t.setDaemon(True)
    t.start()
    t.join()