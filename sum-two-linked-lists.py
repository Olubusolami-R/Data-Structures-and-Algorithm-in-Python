    def sum_two_lists(self, llist):
        p=self.head
        q=llist.head
        cur1=p
        cur2=q
        r=0
        data=0

        #find length of list 1
        counts = 0
        cur_node1 = self.head
        while cur_node1:
            counts += 1
            cur_node1 = cur_node1.next

        #find length of list 2
        countl = 0
        cur_node2 = llist.head
        while cur_node2:
            countl += 1
            cur_node2 = cur_node2.next

        while cur1 and cur2:
            temp=cur1.data+cur2.data+r
            r=0 #reset r back to 0
            if temp>=10:
                r=temp//10 #tens part to be added to next node
                temp=temp%10 #value stored in node(remainder)

            cur1=cur1.next
            cur2=cur2.next

            #check if one of the lists has no next node and create if necessary
            if cur1 and not cur2:
                newnode=Node(data)
                cur2=newnode
            elif cur2 and not cur1:
                newnode=Node(data)
                cur1=newnode

            #store the new list of sums in the bigger list
            if counts>countl:
                p.data=temp
                p=p.next
            else:
                q.data=temp
                q=q.next
                
        if counts>countl:
            return self
        else:
            return llist
        
