class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        max_profit = 0
        
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit,profit)         
            if prices[r] < prices[l] :
                l = r

        return max_profit
        