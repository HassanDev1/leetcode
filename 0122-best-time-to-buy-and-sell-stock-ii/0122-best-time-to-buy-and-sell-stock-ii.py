class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        stack = []
        total = 0
        
        for price in prices:
            if stack and stack[-1] < price:
                buying_p = stack.pop()
                total += price - buying_p
            stack.append(price)
            
        return total
        