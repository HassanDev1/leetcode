class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1]*(len(nums))
        if len(nums)== 1:
            return nums[0]
        
        def get_sum(temp):
            
            prev2 = 0
            prev = temp[0]
            for i in range(1,len(temp)):
                
                take = temp[i]
                take += prev2
                
                not_take = 0+prev
                curr = max(take,not_take)
                
                prev2 = prev
                prev = curr
            return prev
        
      
        
        temp1 = [nums[i] for i in range(1,len(nums))]
       
        temp2 = [nums[i] for i in range(0,len(nums)-1)]
       
        return max(get_sum(temp2),get_sum(temp1))
        