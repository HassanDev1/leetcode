class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        stack = []
        max_area = float("-inf")
        
        
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index,h = stack.pop()
                max_area = max(max_area,(i-index)*h)
                start = index
            stack.append((start,heights[i]))
            
        for i ,h in stack:
            max_area = max(max_area,(len(heights)-i)*h)
        return max_area
                
                
            
        