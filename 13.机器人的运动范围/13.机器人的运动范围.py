# -*- coding:utf-8 -*-
import copy
class Solution:
    def count_sum(self,temp):
        sum = 0
        while(temp%10!=0):
            sum += temp %10
            temp = temp/10
        return sum
    def explore(self,row,col):
        if not (row>=0 and row <self.row and col >=0 and col < self.col):
            return
        if self.count_sum(row)+self.count_sum(col) > self.threshold:
            return
        if self.visit_tag[row][col] == 1:
            return 

        self.ans += 1
        self.visit_tag[row][col] = 1
        self.explore(row,col-1)
        self.explore(row,col+1)

        self.explore(row-1,col)
        self.explore(row+1,col)
        
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.row = rows
        self.col = cols
        self.threshold = threshold
        self.visit_tag = [[0]*cols for i in range(rows)]
        self.ans = 0
        self.explore(0,0)
        return self.ans