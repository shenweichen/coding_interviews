# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        for i in range(1,len(array)):
            array[i] = max(array[i],array[i-1]+array[i])
        return max(array)