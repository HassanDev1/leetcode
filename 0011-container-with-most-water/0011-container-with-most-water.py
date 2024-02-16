class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        most_water = float("-inf")
        l,r =0,len(height)-1
        left_height = height[0]
        right_height = height[r]
        
        while l < r:
            if left_height < right_height:
                most_water = max((r-l)*min(left_height,right_height),most_water)
                
                l +=1
                left_height = height[l]
            else:
                most_water = max((r-l)*min(left_height,right_height),most_water)
                r-= 1
                right_height = height[r]
                
        return most_water
            