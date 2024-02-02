class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        
        check = Counter(nums)
        
        for i, num in enumerate(nums):
            
            if num-1 not in check:
                count = 0
                while count+num in check:
                    count += 1
                longest = max(longest,count)
            
        return longest