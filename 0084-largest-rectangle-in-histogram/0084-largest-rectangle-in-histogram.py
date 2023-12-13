class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        largest = 0
        
        for i,height in enumerate(heights):
            
            start = i
            while stack and stack[-1][1] > height:
                index,h = stack.pop()
                largest = max(largest,(i-index)*h)
                start = index
                
            stack.append((start,height))
            
        for i,h in stack:
            largest = max(largest,(len(heights)-i)*h)
            
        return largest
        