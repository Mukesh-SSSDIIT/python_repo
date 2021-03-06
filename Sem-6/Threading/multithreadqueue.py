import queue
import threading
import time
# Fifo Queue
# q = queue.Queue()
# q = queue.LifoQueue()
q = queue.PriorityQueue()

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

q.put(("adil",t3))
q.put(("abodh",t2))
q.put(("Anil",t4))
q.put(("Zaakash",t1))

while not q.empty():
    item = q.get()
    item[1].start()
    item[1].join()
    # q.task_done()
print("End of program")