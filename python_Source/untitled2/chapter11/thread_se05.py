#-*-coding: utf-8 -*-
import threading
import time

def Mythread(nsleep):
    for i in range(5):
        # print("[%s]%d"%(time.sleep(nsleep)(threading.currentThread().getName(),i)),",nsleep=",nsleep)
        print("[%s]%d"%(threading.currentThread().getName(),i),",nsleep=",nsleep)
        time.sleep(nsleep)

if __name__ == '__main__':
    t1 = threading.Thread(target=Mythread, name="야옹이", args=(0.1,))
    t2 = threading.Thread(target=Mythread, name="멍멍이", args=(0.1,))
    t3 = threading.Thread(target=Mythread, name="꽥꽥이", args=(0.1,))
    t1.start()
    t2.start()
    t3.start()
    main_thread=threading.currentThread()
    while True:
        tlist = threading.enumerate()
        if len(tlist) <= 2:
            break
        for t in tlist:
            if t is main_thread:
                continue
            print(t)
        time.sleep(1)