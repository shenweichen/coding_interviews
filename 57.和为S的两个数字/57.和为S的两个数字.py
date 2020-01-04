# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        i = 0
        j = len(array)-1
        if len(array)<2:
            return []
        while(True):
            if array[i] + array[j] == tsum:
                return [array[i],array[j]]
            elif array[i] + array[j] > tsum:
                j-=1
            else:
                i+=1
            if i==len(array) or j==-1:
                return []