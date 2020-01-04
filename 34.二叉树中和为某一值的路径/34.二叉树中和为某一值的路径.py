# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        self.ans = []
        def Find(temp,root):
            temp.append(root.val)
            if root.left is None and root.right is None:
                if sum(temp) == expectNumber:
                    self.ans.append(temp[:])
            else:
                if sum(temp) > expectNumber:
                    temp.pop()
                    return
                if root.left is not None:
                    Find(temp[:],root.left)
                if root.right is not None:
                    Find(temp,root.right)
        Find([],root)
        return self.ans
                
            