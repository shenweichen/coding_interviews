# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        ss = sorted(list(ss))
        used = [False] * len(ss)
        self.ans = []
        def dfs(temp,used):
            if len(temp) == len(ss):
                self.ans.append("".join(temp))
                return
            for i in range(len(ss)):
                if (i>0 and ss[i] == ss[i-1] and used[i-1]==False) or used[i]:
                    continue
                temp.append(ss[i])
                used[i] = True
                dfs(temp,used)
                temp.pop()
                used[i] = False
        dfs([],used)
        return self.ans