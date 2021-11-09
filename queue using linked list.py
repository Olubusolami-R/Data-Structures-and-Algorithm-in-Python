#code for queue implementation using linked list

#declare the node class and its constructor

class node:

    def __init__(self,data):
        self.data=data
        self.next=None

#declare the queue class
class queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new_node=node(data)
            self.tail.next=new_node
            self.tail=self.tail.next
    
    def dequeue(self):
        if self.head==None:
            print("Queue is empty!")
            return None
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
    
    def display(self):
        if self.head ==None:
            print("queue is empty!")
        else:
            temp=self.head
            print(str(temp.data), end=" ")
            while(temp.next):
                temp=temp.next
                print( " -> " + str(temp.data), end=" ")
            print("\n")    

    def get_head(self):
        if(self.head==None):
            print("Queue is empty")
        else:   
            print(str(self.head.data) + " is the head of the queue")

    def get_tail(self):
        if(self.head==None):
            print("Queue is empty")
            return
        print(str(self.tail.data) + " is the tail of the queue")


    def is_empty(self):
        if self.head==None:
            return True
        return False
    
    def size(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count


q1=queue()

menu=dict()
menu[1]='enqueue'
menu[2]='dequeue'
menu[3]='display'
menu[4]='get head'
menu[5]='get tail'
menu[6]='get size'
menu[7]='quit'

temp=int(input("Enter 1 to start or 0 to quit\n"))
if(temp==1):
    ans=True
else: 
    ans=False

for key in menu:
        print(str(key)+" : "+ menu[key])
while ans:
    input1=int(input("What would you like to do next?\n"))

    if input1==1:
        input2=int(input("Enter value to enqueue:"))
        q1.enqueue(input2)
        print("Success!")
    elif input1==2:
        q1.dequeue()
        print("Success!")
    elif input1==3:
        q1.display()
    elif input1==4:
        q1.get_head()
    elif input1==5:
        q1.get_tail()
    elif input1==6:
        print('The size of the queue is ' +str(q1.size()))
    else:
        ans=False



