class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <1:
            return None
        p = head
        q = head      
        step = 1
        while p.next is not None:
            if step >= k and q is not None:
                q = q.next
            p = p.next
            step += 1

        if k <= step:
            return q.val
        else:
            return -1