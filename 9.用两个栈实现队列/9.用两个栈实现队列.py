# -*- coding:utf-8 -*-
class Solution:
    stack1 = []
    stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if len(self.stack2)==0:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
        xx = self.stack2[-1]
        self.stack2.pop()
        return xx