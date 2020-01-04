# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0])==0:
            return False
        row = len(array)
        col = len(array[0])
        xcol = 0
        xrow = row - 1
        while xrow > -1 and xcol < col:
            x = array[xrow][xcol]
            print x
            if x == target:
                return True
            elif x > target :
                xrow -= 1
            elif x < target :
                xcol += 1
        return False
            
            
            