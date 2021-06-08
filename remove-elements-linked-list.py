# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur=head
        prev=None
        while cur:
            if cur.val==val:
                if cur==head:
                    head=cur.next
                    cur.next=None
                    cur=head
                else:
                    prev.next=cur.next
                    cur.next=None
                    cur=prev.next
                continue   
            prev=cur
            cur=cur.next
                
        return head  
