# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        return self.check(sequence,0,len(sequence)-1)
    def check(self,arr,start,end):
        if start>=end:
            return True
        root = arr[end]
        end = end - 1
        while(end >=0 and arr[end]>root):
            end -= 1
        mid = end + 1
        for i in range(start,mid):
            if arr[i] > root:
                return False
        return self.check(arr,start,mid-1) and self.check(arr,mid,end)