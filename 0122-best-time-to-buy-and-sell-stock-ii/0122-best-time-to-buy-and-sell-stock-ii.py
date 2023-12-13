class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        stack = []
        for i,p in enumerate(prices):
            
            if stack and stack[-1] < p:
                prev_price = stack.pop()
                max_profit += (p - prev_price)
            stack.append(p)
            
        return max_profit
        