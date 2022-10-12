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
print(t.name,'is alive or not',t.is_alive())
l = enumerate()
for t in l:
    print('thread name ',t.name)
    print('thread identification number ',t.ident)
    print()
