# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray) - 1
        mid = low
        while(rotateArray[low]>= rotateArray[high]):
            mid = low + (high - low)//2
            if high - low == 1:
                mid = high
                break
            if rotateArray[mid] == rotateArray[low] and rotateArray[mid] == rotateArray[high]:
                return min(rotateArray[low:high+1])
            elif rotateArray[mid] >= rotateArray[low]:
                low = mid
            elif rotateArray[mid] <= rotateArray[high]:
                high = mid
        return rotateArray[mid]