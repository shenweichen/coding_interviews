# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        i = 0
        while(i<len(s) and s[i]==" "):
                i += 1
        if i == len(s):
            return s
        stack = []
        ans = ""
        i = 0
        while(i<len(s)):
            while(i<len(s) and s[i]==" "):
                i += 1
            temp = ""
            while(i < len(s) and s[i]!=" "):
                temp += s[i]
                i += 1
            stack.append(temp)
        ans += stack.pop()
        while(len(stack)>0):
            ans += " "
            ans += stack.pop()
        return ans
           