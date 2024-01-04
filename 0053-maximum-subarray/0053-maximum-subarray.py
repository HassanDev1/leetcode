class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = sum(nums)
       
        curr_sum = 0
        l = 0
        for r,num in enumerate(nums):
            curr_sum += num
            max_sum = max(max_sum,curr_sum)
            if curr_sum < 0: 
                curr_sum = 0
              
                
        return max_sum
                
            
        