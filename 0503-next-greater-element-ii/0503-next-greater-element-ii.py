class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res = [-1]*len(nums)
        
        j = 0
        stack = []
        while j < 2:
            
            for i,num in enumerate(nums):
                while stack and nums[stack[-1]] < num:
                    res[stack.pop()] = num
                    
                stack.append(i)
            j += 1
        return res
        