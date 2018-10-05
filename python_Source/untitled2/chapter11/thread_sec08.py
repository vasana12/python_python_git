#-*-coding: utf-8 -*-
import threading

def counter(e):
    e.wait()
    for i in range(5):
        print(i)
if __name__=='__main__':
    e = threading.Event()
    t1 = threading.Thread(target=counter, args=(e,))
    t1.start()
    for i in range(100,105):
        print(i)
    e.set()

