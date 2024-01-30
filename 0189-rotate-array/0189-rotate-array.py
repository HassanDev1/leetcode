class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %=len(nums)
        res = nums[0:len(nums)-k]
        last = nums[len(nums)-k:]
        output = last+res
        for i in range(len(nums)):
            nums[i] = output[i]
            
        return nums[i]
        
            
        
        