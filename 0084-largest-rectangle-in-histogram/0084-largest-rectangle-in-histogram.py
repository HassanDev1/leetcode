class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        largest = 0
        
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_index,prev_h = stack.pop()
                area =  (i-prev_index)*prev_h
                largest = max(largest,area)
                start = prev_index
                
            stack.append((start,h))
            
        for i,h in stack:
            area = (len(heights)-i)*h
            largest = max(largest,area)
            
        return largest