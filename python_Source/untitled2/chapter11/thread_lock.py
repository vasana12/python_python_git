import threading
import time

tot =0
lock = threading.Lock()

def add_total(amount):
    global tot
    lock.acquire()
    try:
        time.sleep(1)
        tot+=amount
    finally:
        lock.release()
        pass

    print(threading.currentThread().getName()+'Syncronized:', tot)

if __name__=='__main__':
    for i in range(1,101):
        my_thread=threading.Thread(target=add_total, args=(i,))
        my_thread.start()