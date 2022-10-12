from threading import *
import time

def job():
    for i in range(10):
        print('lazy thread')
        time.sleep(2)

t = Thread(target=job)
t.setDaemon(True) #shows how stopping of no daemon thread also stops daemon thread
t.start()
time.sleep(10)
print('end of main thread')