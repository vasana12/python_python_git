#-*-coding: utf-8 -*-
import threading
import time

def Thread_Test():
    for x in range(5):
        print("python_Threading")

t = threading.Timer(5, Thread_Test)
t.start()
#time.sleep(2)
#t.cancel()