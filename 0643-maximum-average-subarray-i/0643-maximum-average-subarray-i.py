class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        curr_sum = 0
        l = 0
        for r,num in enumerate(nums):
            curr_sum += num
            if r-l+1 >= k:
                max_avg = max(max_avg,curr_sum/k)
                curr_sum -= nums[l]
                l += 1
                
        return max_avg
                