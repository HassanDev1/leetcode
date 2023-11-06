class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = height[0]
        right_max = height[-1]
        l = 0
        r = len(height)-1
        trap = 0
        
        while l < r:
            
            if left_max < right_max:
                l += 1
                
                left_max = max(height[l],left_max)
                trap += left_max - height[l]
                
               
            else:
                r -= 1
                right_max = max(right_max,height[r])
                trap += right_max - height[r]
                
                
                
        return trap
        