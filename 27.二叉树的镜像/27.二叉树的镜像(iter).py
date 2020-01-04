# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        #def preOrder(root):
        #    if root is not None:
        #        root.left,root.right = root.right,root.left
        #        preOrder(root.left)
        #        preOrder(root.right)
        #preOrder(root)
        if root is None:
            return root
        stack = []
        x = root
        while True:
            while(x is not None):
                stack.append(x)
                x = x.left
            if len(stack) == 0:
                break
            x = stack.pop()
            x.left,x.right = x.right,x.left
            x = x.left
        return root