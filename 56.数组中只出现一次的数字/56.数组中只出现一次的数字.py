# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        result = None
        for num in array:
            if result is None:
                result = num
            else:
                result ^= num
        mask = 1
        while(result&mask==0):
            mask = mask<<1
        ans = [None,None]
        for num in array:
            if num&mask != 0:
                if ans[0] is None:
                    ans[0] = num
                else:
                    ans[0] ^= num
            else:
                if ans[1] is None:
                    ans[1] = num
                else:
                    ans[1] ^= num
        return ans