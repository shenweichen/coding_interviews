# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        self.q = [pRoot]
        ans = []
        row = 1
        while(len(self.q)!=0):
            size = len(self.q)
            l = []
            for i in range(0,size):
                front = self.q.pop(0)
                l.append(front.val)
                if front.left is not None:
                    self.q.append(front.left)
                if front.right is not None:
                    self.q.append(front.right)
            if row&1 == 1:
                ans.append(l[:])
            else:
                ans.append(l[::-1])
            row +=1
        return ans
        