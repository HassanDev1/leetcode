class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix =  1
        res = [0]*len(nums)
        
        for i,num in enumerate(nums):
            res[i] = prefix
            prefix *= num
            
        postfix = 1    
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
            
            
        