class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        two_sum = {}
        
        for i,num in enumerate(nums):
            diff = target - num
            if diff in two_sum:
                return [i,two_sum[diff]]
            
            two_sum[num] = i
            
        
        
        