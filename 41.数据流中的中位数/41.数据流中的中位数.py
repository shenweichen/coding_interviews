# -*- coding:utf-8 -*-
class Heap:
    def __init__(self,cmp_f):
        self.cmp = cmp_f
        self.heap = []
    def siftDown(self,i):
        target= i
        left = 2*i + 1
        right = 2*i + 2
        if left < self.size() and self.cmp(self.heap[left],self.heap[target]):
            target = left
        if right < self.size() and self.cmp(self.heap[right],self.heap[target]):
            target = right
        if target != i:
            self.heap[target],self.heap[i] = self.heap[i],self.heap[target]
            self.siftDown(target)
    def size(self,):
        return len(self.heap)
    def pop(self,):
        if self.size() ==0:
            return None
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        elem = self.heap.pop()
        self.siftDown(0)
        return elem
    def insert(self,num):
        self.heap.append(num)
        i = self.size() - 1
        parent = (i-1)>>1
        while(i>0 and self.cmp(self.heap[i],self.heap[parent])):
            self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]
            i = parent
            parent = (i-1)>>1
        
    def top(self,):
        return self.heap[0]
        
        
class Solution:
    def __init__(self,):
        self.maxHeap = Heap(lambda x,y:x>y)
        self.minHeap = Heap(lambda x,y:x<y)
    def Insert(self, num):
        # write code here
        if self.maxHeap.size() == self.minHeap.size():
                self.minHeap.insert(num)
                self.maxHeap.insert(self.minHeap.pop())
        else:
                self.maxHeap.insert(num)
                self.minHeap.insert(self.maxHeap.pop())
    def GetMedian(self,n=None):
        # write code here
        if self.maxHeap.size() == self.minHeap.size():
            return (self.maxHeap.top()+self.minHeap.top())/2.0
        else:
            return self.maxHeap.top()*1.0
    