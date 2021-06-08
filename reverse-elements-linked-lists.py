class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur=head
        revlist=[]
        count=0
        while cur:
            revlist.append(cur.val)
            cur=cur.next
            count=count+1
        cur=head
        while cur:
            cur.val=revlist[count-1]
            count-=1
            cur=cur.next
            
        return head
