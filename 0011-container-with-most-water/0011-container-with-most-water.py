class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        l,r = 0,len(height)-1
        min_left = height[0]
        min_right = height[-1]
        
        while l < r:
            area = (r-l)*min(min_left,min_right)
            max_area = max(area,max_area)
            
            if min_left < min_right:
                l += 1
                min_left = height[l]
            else:
                r -= 1
                min_right = height[r]
                
        return max_area
        