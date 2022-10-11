import time
from threading import *

def test():
    print(current_thread().name,'....started')
    time.sleep(3)
    print(current_thread().name,'....ended')

print('active thread are :',active_count())
t = Thread(target=test, name='childthread')
t1 = Thread(target=test, name='childthread1')
t2 = Thread(target=test, name='childthread2')
t.start()
t1.start()
t2.start()
print('active thread again :',active_count())
time.sleep(10)
print('active thread after 10 sec :',active_count())