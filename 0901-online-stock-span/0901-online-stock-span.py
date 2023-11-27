class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []
        

    def next(self, price: int) -> int:
        span = 1
        stack = self.monotonic_stack
        
        while stack and stack[-1][0] <= price:
            _,curr_span = stack.pop()
            span += curr_span
        stack.append((price,span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)