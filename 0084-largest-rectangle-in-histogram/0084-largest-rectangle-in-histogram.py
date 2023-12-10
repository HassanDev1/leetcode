class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        
        stack = []
        # i= 2 h=5 
        #stack = [(0,2)]
        #max_area = 1
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,prev_h = stack.pop()       #index =0 ,prev_h =2
                max_area = max(max_area,(i-index)*prev_h)  #max_h = 4
                start = index                               #start = 2
                
            stack.append((start,h))
        for i,h in stack:
            max_area = max(max_area,(len(heights)-i)*h)
            
        return max_area
            
        
        