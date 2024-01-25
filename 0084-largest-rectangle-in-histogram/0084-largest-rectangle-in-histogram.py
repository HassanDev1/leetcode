class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        largest = 0
        
        stack = []
        
        for i in range(len(heights)):
            
            start = i
            while stack and stack[-1][1] > heights[i]:
                prev_index,prev_h = stack.pop()
                area = (i-prev_index)*prev_h
                largest = max(largest,area)
                start = prev_index
                
            stack.append((start,heights[i]))
            
        for i,h in stack:
            largest = max(largest,(len(heights)-i)*h)
            
        return largest