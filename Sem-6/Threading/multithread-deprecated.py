import _thread
from time import *
def hello(message,):
    for i in range(5):
        print(message)
        sleep(1)
def hi(message):
    for i in range(5):
        print(message)
        sleep(1)       
try:
    _thread.start_new_thread(hello,("Hello",))
    _thread.start_new_thread(hi,("Hi",))
    print("No error")
except:
   print ("Error: unable to start thread")
print("Bye")
# while 1:
#     pass
sleep(10)