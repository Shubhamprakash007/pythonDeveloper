from threading import *
def child():
    print('executed by child')
    
t = Thread(target=child)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())
#but if we have started t by t.start() then its daemon nature cant be changed