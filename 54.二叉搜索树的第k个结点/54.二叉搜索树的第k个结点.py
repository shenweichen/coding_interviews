# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k ==0 or pRoot is None:
            return None
        stack = []
        cur = pRoot
        while(True):
            while(cur is not None):
                stack.append(cur)
                cur = cur.left
            if len(stack) == 0:
                break
            cur = stack.pop()
            k -= 1
            if k ==0:
                break
            cur = cur.right
        return cur