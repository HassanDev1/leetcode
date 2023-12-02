class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []
        

    def next(self, price: int) -> int:
        stack = self.monotonic_stack
        
        span = 1
        while  stack and stack[-1][1] <= price:
            prev_span,prev_price = stack.pop()
            span += prev_span
        stack.append((span,price))
        
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)