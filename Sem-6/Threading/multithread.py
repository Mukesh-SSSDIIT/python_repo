import threading
from time import sleep
class C1(threading.Thread):
    def __init__(self,a,b): # Overriding Thread class(baseclass) __init__ method
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
    def run(self): # Overriding Thread class(baseclass) run method
        for i in range(5):
            print("Sum",self.a+self.b)
            sleep(1)

class C2(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
obj1 = C1(5,6)
obj2 = C2()
obj1.start()
obj2.start()
obj1.join()
obj2.join()

print("Bye")