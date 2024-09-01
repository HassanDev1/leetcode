class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        
        def helper(n):
        
            if n == 0 or n == 1:
                return 0
            if n == 2:
                return 1
            if n in memo:
                return memo[n] 
            
            memo[n] = helper(n-1) + helper(n-2) + helper(n-3)
          
            return memo[n]
        return helper(n+1)
        
        