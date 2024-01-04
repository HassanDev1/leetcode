class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        stack = []
        largest = 0
        
        for i in range(len(heights)):
            prev_ind = i
            while stack and stack[-1][1] > heights[i]:
                ind,prev_h = stack.pop()
                largest = max(largest,(i-ind)*prev_h)
                prev_ind = ind
            
            
            stack.append((prev_ind,heights[i]))
            
        for i,h in stack:
            largest = max(largest,(len(heights)-i)*h)
            
        return largest
        