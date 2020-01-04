# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        self.depth = 1
        def preOrder(root,depth):
            if root is None:
                return
            if root.left is None and root.right is None:
                self.depth = max(self.depth,depth)
                return
            preOrder(root.left,depth+1)
            preOrder(root.right,depth+1)
        preOrder(pRoot,1)
        return self.depth