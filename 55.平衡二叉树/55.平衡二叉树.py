# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.isBalance = True
        if pRoot is None:
            return True
        def postOrder(root,):
            if self.isBalance is False:
                return -1
            if root is None:
                return 0
            left = postOrder(root.left)
            right = postOrder(root.right)
            if abs(left - right) > 1:
                self.isBalance = False
            
            return max(left,right) + 1
        postOrder(pRoot)
        return self.isBalance