class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = sum(nums)
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            largest = max(largest,curr_sum)
            if curr_sum < 0:
                curr_sum = 0
                
        return largest