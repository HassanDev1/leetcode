class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r =0,len(height)-1
        
        max_area = 0
        
        while l < r:
            if height[l] < height[r]:
                area = (r-l)*min(height[l],height[r])
                max_area = max(area,max_area)
                l += 1
            else:
                area = (r-l)*min(height[l],height[r])
                max_area = max(area,max_area)
                r -= 1
                
        return max_area
        