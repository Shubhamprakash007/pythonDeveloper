from threading import *
def test():
    print('child thread')

t = Thread(target=test)
t.start()

print('main thread identification number:',current_thread().ident)
print('child thread identification number:',t.ident)