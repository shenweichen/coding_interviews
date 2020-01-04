# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s)==0:
            return s
        s = list(s)
        def flip(s,start,end):
            for i in range(start,(start+end)//2 + 1):
                s[i],s[end-i+start] = s[end - i+start],s[i]
            return s
        n %= len(s)
        s = flip(s,0,n-1)
        s = flip(s,n,len(s)-1)
        s = flip(s,0,len(s)-1)
        return "".join(s)