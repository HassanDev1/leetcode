class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]
            min_coins = float("inf")
            for coin in coins:
                ans = helper(amount-coin)+1
                min_coins = min(ans,min_coins)
                
            memo[amount] = min_coins
            return min_coins
        res = helper(amount)
        if res == float("inf"):
            return -1
        return res
                
            
        