# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 ==None and pHead2 ==None:
            return None
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        p = pHead2.next
        q = pHead1
        front = pHead2
        if(pHead1.val<pHead2.val):
            front = pHead1
            p = pHead1.next
            q = pHead2
        head = front
        while(p!=None and q!=None):
            if(q.val<p.val):
                temp = q.next
                q.next = p
                front.next = q
                front = q
                q=temp
            else:
                front = front.next
                p = p.next
        if(q!=None):
			front.next = q            
                
        return head