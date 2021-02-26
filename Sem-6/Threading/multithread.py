from threading import *
from time import sleep
class C1(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class C2(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            # sleep(1)
obj1 = C1()
obj2 = C2()
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("Bye")