class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r =0,len(height)-1
        max_left = height[0]
        max_right = height[-1]
        trap = 0

        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left,height[l])
                trap += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right,height[r])
                trap += max_right - height[r]
                r -= 1
                
        return trap