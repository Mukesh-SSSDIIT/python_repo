import threading, queue
import time
q = queue.Queue()
def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()
# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(5):
    q.put(item)

print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')
