n=10
class queue:
    def __init__(self):
        self.head=-1
        self.tail=-1
        self.q=[0]*n
    
    def enqueue(self,data):
       if (self.head==-1) and (self.tail==-1):
           self.head=self.tail=(self.head+1)%(n-1)
           self.q[self.head]=data
       else:
           newtail=(self.tail+1)%(n-1)
           if newtail!=self.head:
               self.tail=newtail
               self.q[self.tail]=data
           else:
               print("Queue is full o!")

    def dequeue(self):
        if (self.head==-1) and (self.tail==-1):
            print("Queue is empty!")
        elif self.head==self.tail:
            self.head=self.tail=-1
        else:
            newhead=(self.head+1)%(n-1)
            self.head=newhead
    
    def display(self):
        if self.head ==-1:
            print("queue is empty!")
        else:
            count=self.head
            print(str(self.q[count]), end=" ")
            while(count!=self.tail):
                count=(count+1)%(n-1)
                print( " -> " + str(self.q[count]), end=" ")
            print("\n")    

    def is_empty(self):
        if (self.head==-1) and (self.tail==-1):
            return True
        return False

#testing
q= queue()
print(q.is_empty())
q.enqueue(5)
q.enqueue(3)
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.enqueue(1)
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.display()
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
q.display()
q.dequeue()
q.enqueue(4)
q.display()

q.enqueue(4)
q.display()
print(q.is_empty())