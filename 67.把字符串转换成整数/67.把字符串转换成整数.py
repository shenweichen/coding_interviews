# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0
        i = 0
        while(s[i]==" "):
            i+= 1
        sign = 1
        if s[i] in "+-":
            if s[i] == '+':
                sign = 1
            else:
                sign = -1
            i += 1
        base = 0
        for k in range(i,len(s)):
            if s[k] in "0123456789":
                base = base*10 + int(s[k])
            else:
                return 0
            if base > ((2<<31) - 1):
                base = (2<<31) - 1 if sign == 1 else -(2<<31)
                return base
        return sign*base
            