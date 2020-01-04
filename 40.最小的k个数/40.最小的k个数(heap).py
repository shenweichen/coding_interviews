# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k<=0:
            return []
        def siftDown(arr,i):
            left = 2*i +1
            right = 2*i +2
            maxIndex = i
            if (left < len(arr) and arr[left] > arr[maxIndex]):
                maxIndex = left
            if (right < len(arr) and arr[right] > arr[maxIndex]):
                maxIndex = right
            if (maxIndex!=i):
                arr[i],arr[maxIndex] = arr[maxIndex],arr[i]
                siftDown(arr,maxIndex)
        def heapify(arr):
            for i in reversed(range(0,(len(arr)-2 >>1)+1)):
                siftDown(arr,i)
            return arr
        heap = heapify(tinput[:k])
        for num in tinput[k:]:
            if num < heap[0]:
                heap[0] = num
                siftDown(heap,0)
            
        ans = []
        while(k>0 and len(heap)!=0):
            ans.append(heap[0])
            heap[0] = heap[-1]
            heap.pop()
            siftDown(heap,0)
            k-=1
        return ans[::-1]
            