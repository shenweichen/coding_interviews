# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def cmp(a,b):
            num1 = int(str(a)+str(b))
            num2 = int(str(b)+str(a))
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            else:
                return 0
        numbers.sort(cmp)
        return "".join(str(num)for num in numbers)