class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        largest = 0
        stack = []
        
        for i,h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                index,prev_h = stack.pop()
                largest = max(largest,(i-index)*prev_h)
                start = index
            stack.append((start,h))
            
        for i,h in stack:
            largest = max(largest,(len(heights)-i)*h)
            
        return largest
        