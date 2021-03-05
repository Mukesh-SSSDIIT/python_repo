import queue
import threading

# Fifo Queue
q = queue.Queue()
# q = queue.LifoQueue()
# q = queue.PriorityQueue()

def method1():
    print("Thread started")
    while not q.empty():
        item = q.get()
        print(item[1], end='  ')

threading.Thread(target=method1).start()

q.put((1,"Raj"))
q.put((2,"Prakash"))
q.put((3,"Rohit"))
q.put((4,"Manish"))
q.put((5,"Suresh"))
# for i in range(q.qsize()):

print("\n")
print("End of program")