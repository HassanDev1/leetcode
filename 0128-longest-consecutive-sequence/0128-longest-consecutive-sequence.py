class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        seen = set(nums)
        
        for i in range(len(nums)):
            if nums[i]-1 not in seen:
                count = 0
                while nums[i]+count in seen:
                    count += 1
                   
                longest = max(longest,count)
            
        return longest
                
        