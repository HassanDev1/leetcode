class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def get_ways(i):
            if i ==1:
                return 1
            if i == 2:
                return 2
            if dp[i] != -1: return dp[i]
            dp[i] = get_ways(i-1) + get_ways(i-2)
            return dp[i]
        return get_ways(n)
        
        