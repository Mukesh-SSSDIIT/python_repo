import threading
from time import sleep
class C1(threading.Thread):
    def __init__(self,threadname): # Overriding Thread class(baseclass) __init__ method
        threading.Thread.__init__(self)
        self.threadname = threadname
    def run(self): # Overriding Thread class(baseclass) run method
        isacquired = 0
        print("Acquiring Lock : ",self.threadname)
        isacquired = threadlock.acquire()
        if(isacquired==0):
            print("Thread Blocked: ",self.threadname)
        else:
            print("Lock Acquired : ",self.threadname)
        for i in range(5):
            print("Thread: ",self.threadname)
            sleep(1)
        print("Releasing Lock : ",self.threadname)
        threadlock.release()
        print("Lock Released : ",self.threadname)

threadlock = threading.Lock()
obj1 = C1("Thread1")
obj2 = C1("Thread2")
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("Bye")