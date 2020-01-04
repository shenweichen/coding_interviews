# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        matrix = [matrix[i*cols:(i+1)*cols] for i in range(0,rows)]
        if len(matrix) == 0 or len(matrix[0]) == 0 or len(path) == 0:
            return False
        self.res = False
        def dfs(start,visit,row,col):
            if start == len(path):
                self.res = True
                return
            if not (col>=0 and col < len(matrix[0]) and row>=0 and row <len(matrix)):
                return
            if matrix[row][col]!=path[start] or visit[row][col]==True:
                return  
            visit[row][col] = True
            dfs(start+1,visit[:],row-1,col)
            dfs(start+1,visit[:],row+1,col)
            dfs(start+1,visit[:],row,col-1)
            dfs(start+1,visit[:],row,col+1)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visit = [[False for m in range(len(matrix[0]))]for n in range(len(matrix))]
                dfs(0,visit,i,j)
        return self.res