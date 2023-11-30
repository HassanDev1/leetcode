class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_ele = float("inf")
        
        for num in nums:
            min_ele = min(min_ele,num)
            
        return min_ele
        