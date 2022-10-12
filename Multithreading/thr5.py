import time
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print('doubles :' ,2*i)

def squares(numbers):
    for i in numbers:
        time.sleep(1)
        print('squares L', i*i)

numbers = [1,2,3,4,5,6]
starttime = time.time()
doubles(numbers)
squares(numbers)
endtime = time.time()

print('total time to execute both function without multithreading is ',endtime-starttime)
 