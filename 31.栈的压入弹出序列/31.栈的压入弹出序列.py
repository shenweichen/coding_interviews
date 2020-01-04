# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        k = 0
        stack = []
        for num in popV:
            while(k<len(pushV) and( len(stack)==0 or  stack[-1]!=num)):
                stack.append(pushV[k])
                k+=1
            if len(stack)>0 and stack[-1] == num:
                stack.pop()
        if len(stack)!=0:
            return False
        else:
            return True