# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return [] 
        self.q = [pRoot]
        self.ans = []
        
        while(len(self.q)!=0):
            row = []
            size = len(self.q)
            while(size !=0):
                front = self.q.pop(0)
                row.append(front.val)
                size -= 1
                
                if front.left is not None:
                    self.q.append(front.left)
                if front.right is not None:
                    self.q.append(front.right)
            self.ans.append(row[:])
            
        return self.ans
                
            