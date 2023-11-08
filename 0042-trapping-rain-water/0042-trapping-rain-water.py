class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = 0
        right_max = height[-1]
        l,r = 0,len(height)-1
        trap = 0
        
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max,height[l])
                trap += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max,height[r])
                trap += right_max - height[r]
                r -= 1
                
        return trap
        