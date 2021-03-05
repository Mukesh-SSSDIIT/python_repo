import queue
import threading
import time
# Fifo Queue
q = queue.Queue()
# q = queue.LifoQueue()
# q = queue.PriorityQueue()

def method1():
    for i in range(5):
        print("Method 1")

def method2():
    for i in range(5):
        print("Method 2")

def method3():
    for i in range(5):
        print("Method 3")

def method4():
    for i in range(5):
        print("Method 4")

t1 = threading.Thread(target=method1)
t2 = threading.Thread(target=method2)
t3 = threading.Thread(target=method3)
t4 = threading.Thread(target=method4)

q.put((1,t1))
q.put((2,t2))
q.put((3,t3))
q.put((4,t4))

while not q.empty():
    item = q.get()
    item[1].start()
    item[1].join()

print("End of program")