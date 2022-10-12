import time
from threading import *

def test():
    for i in range(10):
        print('im inside for loop')
        time.sleep(3)

t = Thread(target=test)
t.start()

t.join()

for i in range(10):
    print('im main thread')

