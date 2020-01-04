# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        m = 1
        count = 0
        while(m<=n):
            a = n//m
            b = n%m
            count += (a+8)//10 * m 
            if a%10 == 1:
                count += (b+1)
            m*=10
        return count