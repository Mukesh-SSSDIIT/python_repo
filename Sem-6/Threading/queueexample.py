import queue

# Fifo Queue
q = queue.Queue()
for i in range(5):
    q.put(i)
# for i in range(q.qsize()):
while not q.empty():
    item = q.get()
    print(item, end='  ')
print("\n")

#Lifo Queue
q = queue.LifoQueue()

for i in range(5):
    q.put(i)

# for i in range(q.qsize()):
while not q.empty():
    item = q.get()
    print(item,end="  ")

print("\n")

# Priority Queue
q = queue.PriorityQueue()
q.put((4,"Value 4","Value 4S"))
q.put((2,"Value 2","Value 2S"))
q.put((3,"Value 3","Value 3S"))
q.put((0,"Value 0","Value 0S"))
q.put((1,"Value 1","Value 1S"))

while not q.empty():
    item = q.get()
    print(item[1], item[2])

print("\n")