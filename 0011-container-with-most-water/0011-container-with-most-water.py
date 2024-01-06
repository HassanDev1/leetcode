class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,r =0,len(height)-1
        max_area = 0
        while l < r:
            if height[l] < height [r]:
                area = (r-l)*min(height[l],height[r])
                max_area = max(max_area,area)
                l += 1
            else:
                area = (r-l)*min(height[r],height[l])
                max_area = max(max_area,area)
                r -= 1
                
        return max_area