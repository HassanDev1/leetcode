class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_consec = 0
        
        l = 0
        
        
        for r in range(len(nums)):
            
            if nums[r] == 1:
                max_consec = max(r-l+1,max_consec)
            else:
                l = r+1
        return max_consec
        