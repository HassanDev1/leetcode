class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = [0]*len(height)
        right = [0]*len(height)
        trapped = 0
        
        #filling left lst
        left[0] = height[0]
        for i in range(1,len(height)):
            left[i] = max(left[i-1],height[i])
            
        #filling right list
        right[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            right[i] = max(height[i],right[i+1])
            
        for i in range(len(height)):
            min_height = min(left[i],right[i])
           
            trapped += min_height - height[i]
            
        return trapped
        