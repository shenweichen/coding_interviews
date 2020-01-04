# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = [1]*len(A)
        front = 1
        tail = 1
        for i in range(0,len(A)):
            if i > 0:
                front *= A[i-1]
                tail *= A[len(A)-i]
            B[i] *= front
            B[len(A)-i-1] *= tail
        return B