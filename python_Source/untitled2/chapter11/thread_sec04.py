#-*-coding: utf-8 -*-
import threading
import time
def Mythread():
    for i in range(10000):
        print(i)

if __name__ =='__main__':
    t = threading.Thread(target=Mythread)
    t.setDaemon(True)   #mainThread 종료되는 시점에 같이 종료됨

    t.start()           #메인 스레드 종료되면 Daemon으로 설정한 스레드 자동 종료됨(true 일때)
    if t.isAlive():
        print("daemon is alive")
        t.join(0.01)
    # time.sleep(0.1)     #메인 스레드가 0.1초 뒤에 종료되기 때문에 daemon으로 설정한 스레드가 그사이에 실행됨
