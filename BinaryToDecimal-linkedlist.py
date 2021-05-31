# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        cur=head
        binlist=[]
        count=0
        
        while cur:
            binlist.append(cur.val)
            cur=cur.next
            count+=1
        
        j=0
        i=count-1
        sum=0
        
        while i>=0:
            t=binlist[i]
            if t==0:
                j+=1
                i-=1
                continue
            sum+=(t*(2**j))
            j+=1
            i-=1
            
        return sum
     
