class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        start = Counter(nums)
        longest = 0
        
        for i in range(len(nums)):
            if nums[i]-1 not in start:
                count = 0
                while nums[i] + count in start:
                    count += 1
                longest = max(longest,count)
                    
        return longest
        