# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        col_start = 0
        col_end = len(matrix[0]) - 1
        row_start = 0
        row_end = len(matrix) - 1
        ans = []
        while(col_start < col_end and row_start < row_end):
            for i in range(col_start,col_end):
                ans.append(matrix[row_start][i])
            for i in range(row_start,row_end):
                ans.append(matrix[i][col_end])
            for i in reversed(range(col_start+1,col_end+1)):
                ans.append(matrix[row_end][i])
            for i in reversed(range(row_start+1,row_end+1)):
                ans.append(matrix[i][col_start])
            col_start += 1
            col_end -= 1
            row_start += 1
            row_end -= 1
        if col_start == col_end:
            for i in range(row_start,row_end+1):
                ans.append(matrix[i][col_start])
        elif row_start == row_end:
            for i in range(col_start,col_end+1):
                ans.append(matrix[row_start][i])
        return ans