# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code herewww
        def binsearch(arr,target):
            low = 0
            high = len(arr) - 1
            while(low <= high):
                mid = low + (high-low)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        
        cum_sum = [0]
        cur = 0
        for i in range(1,tsum+1):
            cur = i + cum_sum[-1]
            cum_sum.append(cur)
        ans = []
        for i in range(0,tsum):
            t = binsearch(cum_sum,cum_sum[i]+tsum)
            if t == -1:
                continue
            if t - i>=2:
                ans.append(list(range(i+1,t+1)))
        return ans
   