from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, val):
        self.queue.appendleft(val)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop()
        print("Can't dequeue from an empty queue")
        
    def isEmpty(self):
        if len(self.queue):
            return False
        return True
    
    def traverse(self):
        if self.isEmpty():
            print("\nCan't traverse an Empty Queue")
        else:
            print("\nQueue : ", end = " ")
            for i in self.queue:
                print(i, end=" ")
                
    def head(self):
        if not self.isEmpty():
            return self.queue[-1]
        return None
    
    def tail(self):
        if not self.isEmpty():
            return self.queue[0]
        return None
        
q1 = Queue()

while True:
    choice = int(input("\n1.Enqueue \n2.Dequeue \n3.Traverse \n4.IsEmpty \n5.Tail \n6.Head \n7.Exit \n\nEnter Choice : "))
    if choice == 1:
        value = int(input("\nEnter Value to Enqueue : "))
        q1.enqueue(value)        
    elif choice == 2:
        print(f"\nDequeued Element from Queue : {q1.dequeue()}")       
    elif choice == 3:
        q1.traverse()       
    elif choice == 4:
        print(q1.isEmpty())       
    elif choice == 5:
        print(f"\nTail Element is : {q1.tail()}")     
    elif choice == 6:
        print(f"\nHead Element is : {q1.head()}")       
    else:
        break
        exit()