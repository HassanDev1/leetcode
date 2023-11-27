class Solution:
    def trap(self, height: List[int]) -> int:
        trapCount = 0
        max_left,max_right=height[0],height[-1]
        l,r = 0, len(height)-1
        
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left,height[l])
                trapCount += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right,height[r])
                trapCount += max_right - height[r]
                r -= 1
        return trapCount
        