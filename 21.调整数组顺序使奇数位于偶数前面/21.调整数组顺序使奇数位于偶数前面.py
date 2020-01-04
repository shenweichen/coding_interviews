# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        m = len(array)
        k = 0
        for i in range(m):
            if (array[i]%2==1):
                j = i
                while(j>k):
                    array[j],array[j-1] = array[j-1],array[j]
                    j-=1
                k+=1
        return array
            
