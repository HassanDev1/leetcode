class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0
        pdt = 1
        count = 0
        l = 0
        
        for r in range(len(nums)) :
            pdt *= nums[r]
            
            while pdt >= k:
                pdt //= nums[l]
                l += 1
            count += r-l+1
        return count
        