class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        longest = 0
        l = 0
        for r,h in enumerate(heights):
            start = r
            while stack and stack[-1][1] > h:
                index,prev_h = stack.pop()
                longest = max(longest,prev_h*(r-index))
                start = index
           
            stack.append((start,h))
            
        for i,h in stack:
            longest = max(longest,(len(heights)-i)*h)
            
        return longest
        