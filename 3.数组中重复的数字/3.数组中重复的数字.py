# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i, val in enumerate(numbers):
            if i!=val:
                if numbers[numbers[i]]==val:
                    duplication[0] = val
                    return True
                numbers[i] = numbers[val]
                numbers[val] = val
        return False
