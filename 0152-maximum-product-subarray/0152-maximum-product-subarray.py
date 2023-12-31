class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float("-inf")
        
        
        freq = {}
        pdt = 1
        
        for i,num in enumerate(nums):
            pdt *= num
            max_prod = max(max_prod,pdt)
            if pdt == 0:
                pdt = 1
        pdt = 1
        for i in range(len(nums)-1,-1,-1):
            pdt *= nums[i]
            max_prod = max(max_prod,pdt)
            if pdt == 0:
                pdt = 1
                
            
        return max_prod
            
            
        
                
            