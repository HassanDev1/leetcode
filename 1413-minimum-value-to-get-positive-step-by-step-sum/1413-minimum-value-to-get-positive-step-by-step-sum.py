class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        min_start = min(nums)
        
        if min_start < 1:
            return -1*min_start + 1
        return 1