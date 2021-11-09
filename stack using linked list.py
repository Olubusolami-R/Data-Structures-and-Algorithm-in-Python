#code for stack implementation using linked list

#declare the node class and its constructor

class node:

    def __init__(self,data):
        self.data=data
        self.next=None

#declare the stack class
class stack:

    def __init__(self):
        self.head=None
    
    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new_node=node(data)
            new_node.next=self.head
            self.head=new_node
    
    def pop(self):
        if self.head==None:
            print("Stack is empty!")
            return None
        else:
            poppednode=self.head
            self.head=self.head.next
            return poppednode.data
    
    def display(self):
        if self.head ==None:
            print("Stack is empty!")
        else:
            temp=self.head
            print(str(temp.data), end=" ")
            while(temp.next):
                temp=temp.next
                print( " -> " + str(temp.data), end=" ")
            print("\n")

    def peek(self):
        if self.head==None:
            print("stack is empty!")
        else:
            print("The top element is " + str(self.head.data))

    def check_element(self,position):
        if self.head==None:
            print("Stack is empty!")
        else:
            i=1
            temp=self.head
            while temp:
                if(i==position):
                    print("The element at position "+ str(position) +" is "+str(temp.data))
                    return
                temp=temp.next
                i+=1
        print("Element position does not exist") 

    def is_empty(self):
        if self.head==None:
            return True
        return False

stack1=stack()

menu=dict()
menu[1]='push'
menu[2]='pop'
menu[3]='display'
menu[4]='peek'
menu[5]='check element in specific position'
menu[6]='check if stack is empty'
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
        stack1.push(input2)
        print("Success!")
    elif input1==2:
        print("Element popped is: "+ str(stack1.pop()))
    elif input1==3:
        stack1.display()
    elif input1==4:
        stack1.peek()
    elif input1==5:
        input2=int(input("Enter position to check:"))
        stack1.check_element(input2)
    elif input1==6:
        print(stack1.is_empty())
    else:
        ans=False