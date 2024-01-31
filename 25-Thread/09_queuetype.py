import queue

q=queue.Queue()
q.put(20)
q.put(30)
q.put(40)
q.put(10)
q.put(50)
while not q.empty():
    print(q.get(),end=' ')
    
print()

lq=queue.LifoQueue()
lq.put(20)
lq.put(30)
lq.put(40)
lq.put(10)
lq.put(50)
while not lq.empty():
    print(lq.get(),end=' ')
    
print()
pq=queue.PriorityQueue()
pq.put((20, "A"))
pq.put((30, "B"))
pq.put((40, "C"))
pq.put((10, "D"))
pq.put((50, "E"))
while not pq.empty():
    print(pq.get(),end=' ')
    
    