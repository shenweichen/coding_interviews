# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count = dict()
        for c in s:
            count[c] = count.get(c,0) + 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1