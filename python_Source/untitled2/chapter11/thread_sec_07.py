#-*-coding: utf-8 -*-
import threading
import time

def Thread_Test():
    print("[%s] my python!!" % threading.currentThread().getName())
    t=threading.Timer(1,Thread_Test)#일정 시간 마다 반복 실행
    t.start()

if __name__ == '__main__':
    t = threading.Thread(target=Thread_Test)
    t.start()