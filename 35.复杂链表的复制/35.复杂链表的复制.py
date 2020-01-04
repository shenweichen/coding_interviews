# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        hashset = dict()
        p = pHead
        helpHead = RandomListNode(-1)
        q = helpHead
        while(p is not None):
            newNode = RandomListNode(p.label)
            hashset[p] = newNode 
            q.next = newNode
            q = q.next
            p = p.next
        p = pHead
        q = helpHead.next
        while(p is not None):
            q.random = hashset.get(p.random,None)
            p = p.next
            q = q.next
        return helpHead.next
            