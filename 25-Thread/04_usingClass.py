from threading import*
from time import sleep

class MyThread:
    
    def displayNumber(self):
        i=0
        print(current_thread().getName())
        sleep(1)
        while(i<=10):
            print(i)
            i+=1


obj =MyThread()
t1 = Thread(target=obj.displayNumber)
t1.start()

t2 = Thread(target=obj.displayNumber)
t2.start()

t3 = Thread(target=obj.displayNumber)
t3.start()