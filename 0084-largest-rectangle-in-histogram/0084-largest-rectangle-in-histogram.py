class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        
        largest = 0
        
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] >= heights[i]:
                prev_index,prev_h = stack.pop()
                area = (i - prev_index)*prev_h
                largest = max(largest,area)
                start = prev_index
            stack.append((start,heights[i]))
            
        for i,h in stack:
            area = (len(heights)-i)*h
            largest = max(area,largest)
            
        return largest
             