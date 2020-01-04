# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self,):
        self.d = dict()
        self.count = 0
    def FirstAppearingOnce(self):
        # write code here
        ans = float("inf")
        cha = "#"
        for k,v in self.d.items():
            if v !=-1 and v < ans:
                cha = k
                ans = v
        return cha
                
    def Insert(self, char):
        # write code here
        if char not in self.d:
            self.d[char] = self.count
        else:
            self.d[char] = -1
        self.count += 1