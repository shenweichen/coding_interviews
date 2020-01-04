# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    def __init__(self):
        self.subtree = False

    def check(self,A,B):
        if self.subtree==False:
            return None
        if B.left==None and B.right ==None:
            return None
        if B.left != None :
            if A.left!=None and B.left.val == A.left.val:
                self.check(A.left,B.left)
            else:
                self.subtree = False
        if B.right!=None:
            if A.right != None and B.right.val == A.right.val:
                self.check(A.right,B.right)
            else:
                self.subtree=False
            
    def PreOrder(self,Root):
        if self.subtree:
            return None
        if Root == None:
            return None
        if Root.val == self.target.val:
            self.subtree = True
            self.check(Root,self.target)
        if Root.left != None:
            self.PreOrder(Root.left)
        if Root.right != None:
            self.PreOrder(Root.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None or pRoot1==None:
            return False
        self.target = pRoot2
        self.PreOrder(pRoot1)
        return self.subtree