class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack  = self.stack
        span = 1
        while stack and stack[-1][1] <= price:
            curr_span,p = stack.pop()
            span += curr_span
        stack.append((span,price))
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)