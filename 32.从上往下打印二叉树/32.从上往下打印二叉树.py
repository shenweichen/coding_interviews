# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        from Queue import deque
        ans = []
        queue = deque()
        if root is None:
            return ans
        queue.append(root)
        while(len(queue)!=0):
            x = queue.popleft()
            ans.append(x.val)
            if x.left is not None:
                queue.append(x.left)
            if x.right is not None:
                queue.append(x.right)
        return ans