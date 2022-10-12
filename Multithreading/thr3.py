#secong way of creating multithreadin in python by oop style
from threading import *
class MyThread(Thread):
    #mythread is child class of Thread class we need to overwrite which method run in java ig
    def run(self):
        for i in range(10):
            print('run by MyThread or child thread')

t = MyThread()  #creation of instance
t.start()

#now after start two threads are there
#below all code is executed by main thread 

for i in range(10):
    print('main thread')