class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = {}
        stack = []
        
        res = []
        
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                next_greater[stack.pop()] = nums2[i]
                
            stack.append(nums2[i])
            
        for num in stack:
            next_greater[num] = -1
            
        for num in nums1:
            res.append(next_greater[num])
            
        return res
            
        
        
        
        