def pairs_with_sum(self, sum_val):  
    cur1=self.head
    cur2=self.head
    strlist=[]
    
    while cur1:
      cur2=cur1
      while cur2:

        if (cur1.data+cur2.data)==sum_val:
          a=str(cur1.data)

          b=str(cur2.data)

          c="("+a+","+b+")"

          strlist.append(c)
          
        cur2=cur2.next

      
      cur1=cur1.next

    return strlist
