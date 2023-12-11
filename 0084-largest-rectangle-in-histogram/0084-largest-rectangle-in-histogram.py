class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0
        
        for i,h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                index,prev_h = stack.pop()
                max_area = max(max_area,(i-index)*prev_h)
                start = index
                
            stack.append((start,h))
            
        for i,h in stack:
            max_area = max(max_area,(len(heights)-i)*h)
            
        return max_area
        