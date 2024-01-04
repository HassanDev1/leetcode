class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        count = 0
        l = 0
        for r,num in enumerate(nums):
            if num == 0:
                count += 1
                while count > k:
                    if nums[l] == 0:
                        count -= 1
                    l += 1
            longest = max(longest,r-l+1)
        return longest  
                
        