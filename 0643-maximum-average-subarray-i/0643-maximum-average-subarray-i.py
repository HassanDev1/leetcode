class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        l = 0
        max_avg = float("-inf")
        curr_sum = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            if r-l+1 >=k:
                avg = curr_sum / k
                max_avg = max(avg,max_avg)
                curr_sum -= nums[l]
                l += 1
        return max_avg
            
        