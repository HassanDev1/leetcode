class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = height[0]
        right_max = height[-1]
        l,r =0,len(height)-1
        trapped = 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max,height[l])
                trapped += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max,height[r])
                trapped += right_max - height[r]
                r -= 1
                
        return trapped
        