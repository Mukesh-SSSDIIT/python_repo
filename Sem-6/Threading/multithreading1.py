from threading import *
from time import *

def hello():
    for i in range(5):
        print("Hello")
        sleep(1)

def hi():
    for i in range(5):
        print("Hi")
        sleep(1)       

Thread(target=hello).start()
Thread(target=hi).start()