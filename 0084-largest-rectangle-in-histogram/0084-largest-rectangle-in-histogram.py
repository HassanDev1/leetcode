class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        largest = 0
        l = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index,prev_h = stack.pop()
                area = prev_h*(i-index)
                largest = max(area,largest)
                start = index
                
            stack.append((start,heights[i]))
        
        
        for i,h in stack:
            largest = max(largest,h*(len(heights)-i))
            
        return largest