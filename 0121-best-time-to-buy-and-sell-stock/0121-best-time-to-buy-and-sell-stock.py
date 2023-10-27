class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0
        
        l = 0
        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_prof = max(max_prof,prices[r]-prices[l])
            
        return max_prof
        