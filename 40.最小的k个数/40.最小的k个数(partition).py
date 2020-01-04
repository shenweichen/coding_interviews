# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or len(tinput)==0 or k<=0:
            return []
        if k == len(tinput):
            return sorted(tinput)
        def partition(arr,start,end):
            pivot = arr[end]
            i = start
            j = end
            while(i<j):
                while(i<j and arr[i]<=pivot):
                    i += 1
                arr[j] = arr[i]
                while(i<j and arr[j]>=pivot):
                    j -= 1
                arr[i] = arr[j]
            arr[i] = pivot
            return i
        start = 0
        end = len(tinput) - 1
        index = partition(tinput,start,end)
        while(index != k-1):
            if index > k-1:
                end = index - 1
                index = partition(tinput,start,end)
            else:
                start = index + 1
                index = partition(tinput,start,end)
        return sorted(tinput[:k])