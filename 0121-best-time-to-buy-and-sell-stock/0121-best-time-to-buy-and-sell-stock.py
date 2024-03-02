class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        max_profit = 0
        left = 0
        for right in range(1,len(prices)):
            
            if prices[right] < prices[left]:
                left = right
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit,max_profit)
            
        return max_profit