# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        ans = []
        small = 1
        big = 2
        cur = 3
        while(small <= (tsum-1)//2):
            if cur == tsum:
                ans.append(list(range(small,big+1)))
                cur -= small
                small += 1
            elif cur > tsum:
                cur -= small
                small += 1
            else:
                big += 1
                cur += big
        return ans