# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        stack = []
        cur = pRootOfTree
        prev = None
        head = None
        while(True):
            while(cur is not None):
                stack.append(cur)
                cur = cur.left
            if len(stack) == 0:
                break
            cur = stack.pop()
            if prev is None:
                cur.left = None
                head = cur
            else:
                prev.right = cur
                cur.left = prev
            prev = cur
            cur = cur.right
        return head