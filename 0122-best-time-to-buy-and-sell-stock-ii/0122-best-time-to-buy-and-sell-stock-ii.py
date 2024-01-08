class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        
        for r in range(1,len(prices)):
            if prices[r] > prices[l]:
                max_profit += prices[r]- prices[l]
            l += 1
        return max_profit
        