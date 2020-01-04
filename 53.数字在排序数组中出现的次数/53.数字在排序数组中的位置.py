# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return 0
        lo = 0
        hi = len(data) - 1
        while(lo < hi):
            mid = lo + (hi-lo)//2
            if data[mid] >= k:
                hi = mid
            else:
                lo = mid + 1
        if data[lo] !=k:
            return 0
        start = lo
        lo = 0
        hi = len(data) - 1
        while(lo < hi):
            mid = lo + (hi-lo)//2
            if data[mid] > k:
                hi = mid
            else:
                lo = mid + 1
        if lo == len(data) -1:
            lo += 1
        return lo - start