class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # step_1, step_2 = 0, 0
        # for i in nums:
        #     curr = max(step_1 + i, step_2)
        #     step_1 = step_2
        #     step_2 = curr
        # return curr
    
        dp = [-1]*(len(nums))
        
        def dfs(i,dp,temp):
            # if i == 0:return temp[i]
            if i < 0 : return 0
            if dp[i] != -1: return dp[i]

            take = temp[i] + dfs(i-2,dp,temp)
            not_take = 0 + dfs(i-1,dp,temp)

            dp[i] = max(take,not_take)
            return dp[i]
        
        return dfs(len(nums)-1,dp,nums)
        
#         temp1 = [nums[i] for i in range(1,len(nums))]
       
#         temp2 = [nums[i] for i in range(0,len(nums)-1)]
       
#         return max(dfs(len(temp1)-1,dp,temp1),dfs(len(temp2)-1,dp,temp2))