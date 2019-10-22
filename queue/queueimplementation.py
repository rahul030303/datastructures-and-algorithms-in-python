import timeit

start = timeit.default_timer()

#Your statements here


class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items) 
    def display(self):
        print([i for i in self.items])

        
q1 = Queue()
q1.enqueue(19)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(34)
q1.dequeue()
q1.display()

stop = timeit.default_timer()
timeTaken = stop - start
print('Time: ', timeTaken)  


