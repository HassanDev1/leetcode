class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        
        b = 0
        max_profit = 0
        for s in range(1,len(prices)):
            curr_profit = prices[s] - prices[b]
            if curr_profit <= 0:
                b = s
            max_profit = max(max_profit,curr_profit)
        return max_profit