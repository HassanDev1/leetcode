class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        startp = Counter(nums)
        longest = 0
        
        for num in nums:
            
            if num- 1 not in startp:
                count = 0
                while num + count in startp:
                    count += 1
                longest = max(longest,count)
                
        return longest
            
                
        
        