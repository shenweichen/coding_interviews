# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.minstack)==0:
            self.minstack.append(node)
        elif node <= self.min():
            self.minstack.append(node)
    def pop(self):
        # write code here
        node = self.stack.pop()
        if node == self.min():
            self.minstack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]