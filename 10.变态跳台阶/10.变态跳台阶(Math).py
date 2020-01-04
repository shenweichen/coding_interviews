# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = [0,1,2]
        for i in range(3,number+1):
            dp.append(sum(dp)+1)
        return dp[number]
            