class Solution:
    def fib(self, n: int) -> int:
        
        zero,one = 0,1
        if n == 0:
            return zero
        if n == 1:
            return one
        
        for i in range(2,n+1):
            curr = zero + one
            zero,one = one,curr
        return one
        