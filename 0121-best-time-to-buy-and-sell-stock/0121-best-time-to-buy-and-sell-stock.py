class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        l = 0
        max_prof = float("-inf") 
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l  = r
                
            curr_profit = prices[r] - prices[l]
            max_prof = max(max_prof,curr_profit)
            
        return max_prof
        