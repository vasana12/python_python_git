#-*-coding: utf-8 -*-
#Thread객체 생성 자의 매개인자로 스레드 대상, 스레드 이름, 타겟을 호출할 때의 인수 등을 전달함과
#동시에 여러개의 스레드를 실행시키는 코드이다.

import threading
import time
lock = threading.Lock()
def Mythread(nsleep):
    lock.acquire()
    for i in range(5):
        print("[%s]%d" % (threading.currentThread().getName(),i))
        print(nsleep)
        time.sleep(nsleep)
    lock.release()
if __name__=='__main__':
    t1 = threading.Thread(target=Mythread, name="야옹이",args=(0.1,))
    t2 = threading.Thread(target=Mythread, name="멍멍이",args=(0.2,))
    t3 = threading.Thread(target=Mythread, name="꽥꽥이",args=(0.3,))
    t1.start()
    t2.start()
    t3.start()