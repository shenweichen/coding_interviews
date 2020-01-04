# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        num = numbers[0]
        times = 1
        for val in numbers[1:]:
            if times == 0:
                num = val
                times = 1
            elif val == num:
                times +=1 
            else:
                times -=1
            print(val,times)
        
        max_times = 0
        for val in numbers:
            if val == num:
                max_times+=1
        if max_times > len(numbers)/2:
            return num
        else:
            return 0