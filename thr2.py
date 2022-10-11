import threading

def thr2():
    print('child thread value :',threading.current_thread().getName())
    print('\n')

obj = threading.Thread(target=thr2)
obj.start()

print('main thread name :',threading.current_thread().getName())