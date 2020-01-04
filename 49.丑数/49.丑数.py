# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        dp = [1]
        t2 = t3 = t5 = 0
        for i in range(index):
            ugly = min(min(dp[t2]*2,dp[t3]*3),dp[t5]*5)
            if ugly == dp[t2]*2:
                t2+=1
            if ugly == dp[t3]*3:
                t3+=1
            if ugly == dp[t5]*5:
                t5+=1
            dp.append(ugly)
        return dp[index-1]