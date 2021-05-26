def move_tail_to_head(self):
        prev=None
        q=self.head
        p=self.head
        while q.next:
            prev=q
            q=q.next
        self.head=q
        q.next=p
        prev.next=None
        
