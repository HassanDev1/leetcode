class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        
        seen = Counter(nums)
        
        for num in nums:
            if num-1 not in seen:
                count = 0
                while num + count in seen:
                    count += 1
                longest = max(longest,count)
                
        return longest
        