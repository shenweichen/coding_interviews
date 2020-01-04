# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <=2:
            return []
        import math
        ans = []
        for n in range(int(1+math.sqrt(1+8*tsum))//2-1,max(int(1-math.sqrt(1+8*tsum))//2,1),-1):
            if 2*tsum%n==0 :
                if (2*tsum-n*n+n)%(2*n) == 0:
                    a = (2*tsum-n*n+n)//(2*n)
                    ans.append(list(range(a,a+n)))
        return ans