class Solution:
    def trap(self, height: List[int]) -> int:
        
        trap = 0
        max_left = height[0]
        max_right = height[-1]
        left,right = 0,len(height)-1
        
        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left,height[left])
                trap += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right,height[right])
                trap += max_right - height[right]
                right -= 1
                
        return trap
                
        