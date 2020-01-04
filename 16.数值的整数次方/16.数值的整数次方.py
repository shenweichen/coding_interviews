# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if abs(base - 0)<1e-7 and exponent < 0:
            return 0
        absExponent = abs(exponent)
        def PowerWithUnsigned(base,exponent):
            if exponent == 0:
                return 1
            if exponent == 1:
                return base
            result = PowerWithUnsigned(base,exponent>>1)
            result*=result
            if exponent&1 == 1:
                result*=base
            return result
        result = PowerWithUnsigned(base,absExponent)
        if exponent < 0:
            result = 1/result
        return result