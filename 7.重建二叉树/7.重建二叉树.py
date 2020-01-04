# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        root = TreeNode(pre[0])
        index = tin.index(root.val)
        leftNum = index
        rightNum = len(tin) - leftNum - 1
        root.left = self.reConstructBinaryTree(pre[1:1+leftNum],tin[0:leftNum])
        root.right = self.reConstructBinaryTree(pre[1+leftNum:],tin[leftNum+1:])
        return root