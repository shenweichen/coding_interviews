# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None
        count1 = 0
        count2 = 0
        p = pHead1
        while(p is not None):
            p = p.next
            count1 += 1
        p = pHead2
        while(p is not None):
            p = p.next
            count2 += 1
        if count1 > count2:
            p = pHead1
            q = pHead2
        else:
            p = pHead2
            q = pHead1
        count = abs(count1 - count2)
        while(count > 0):
            p = p.next
            count -= 1
        while(p!=q):
                p = p.next
                q = q.next
        return p
        
        