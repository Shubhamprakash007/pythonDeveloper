#creating thread by using normal class
from threading import *

class Test:
    def m1(self):
        for i in range(10):
            print('by using normal class')

obj = Test()
t = Thread(target = obj.m1)
t.start()

for i in range(10):
    print('main thread')