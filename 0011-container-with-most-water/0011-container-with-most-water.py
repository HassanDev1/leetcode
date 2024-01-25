class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        l,r = 0,len(height)-1
        max_height = 0
        
        while l < r:
            if height[l] < height[r]:
                area = (r-l)*min(height[l],height[r])
                max_height = max(area,max_height)
                l += 1
            else:
                area = (r-l)*min(height[l],height[r])
                max_height = max(area,max_height)
                r -= 1
                
        return max_height