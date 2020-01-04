# -- codingutf-8 --
class Solution
    def Fibonacci(self, n)
        # write code here
        f = [0,1]
        if n 2
            return f[n]
        for i in range(2,n+1)
            f.append(f[i-1] +f[i-2])
        return f[n]