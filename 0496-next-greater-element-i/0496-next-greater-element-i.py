class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = {}
        stack = []
        res = []
        
        for num in nums2:
            
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
            
        for num in stack:
            next_greater[num] = -1
            
      
            
        for num in nums1:
            res.append(next_greater[num])
            
        return res
            
        