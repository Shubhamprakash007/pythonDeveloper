#1 st way of creating multithreading in python 

import threading
def thr():
    for i in range(10):
        print('child thread execution\n')

obj = threading.Thread(target=thr) #creation of thread by extending thread class or by using thread object
obj.start()

# def thr1():
#     for i in range(10):
#         print('another thread child class')

# obj1 = threading.Thread(target=thr1)
# obj1.start()

for i in range(10):
    print('\nexecuted by main thread')

