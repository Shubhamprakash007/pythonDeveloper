import time, threading
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print('doubles :' ,2*i)

def squares(numbers):
    for i in numbers:
        time.sleep(1)
        print('squares L', i*i)

numbers = [1,2,3,4,5,6]
start = time.time()
t1 = threading.Thread(target=doubles,args=(numbers,))
t2 = threading.Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
#after start all line will be executed by main thread it will not wait for child thread
t1.join() #main thread execution after t1
t2.join()
#we have to specify if we want to execute main thread after child thread
end = time.time()

print('total time to execute both function with multithreading is  ',end-start)
 