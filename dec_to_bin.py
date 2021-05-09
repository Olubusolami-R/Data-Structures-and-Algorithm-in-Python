class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def convert(dec_num):
  ans=""
  st=Stack()
  while dec_num!=0:
    temp=dec_num%2
    dec_num=dec_num//2
    st.push(temp)
  while not st.is_empty():
    ans+=str(st.pop())
  return ans

print(convert(53))
