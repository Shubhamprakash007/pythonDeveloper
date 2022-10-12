from threading import *
import time
def t1():
    print('executed by t1')
    job2=Thread(target=t2)
    print('is job2 daemon ',job2.isDaemon())
    job2.start()

def t2():
    print('executed by t2')

job1 = Thread(target=t1)
job1.setDaemon(True)
print('is job1 daemon ',job1.isDaemon())
job1.start()
time.sleep(10)
