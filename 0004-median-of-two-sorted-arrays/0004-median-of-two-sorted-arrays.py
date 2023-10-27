class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        sorted_nums = sorted(nums1+nums2)
        
        size = len(sorted_nums)
        median = 0
        
        if size % 2 == 0:
            mid = size//2
            median = (sorted_nums[mid-1] + sorted_nums[mid]) / 2.0
        else:
            mid = size//2
            median = sorted_nums[mid]
            
        return median
        