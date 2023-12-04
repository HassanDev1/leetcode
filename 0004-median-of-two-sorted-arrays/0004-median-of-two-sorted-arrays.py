class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        sorted_list = sorted(nums1+nums2)
        
        combined_len = len(nums1) + len(nums2)
        
        if combined_len % 2 == 0:
            mid = (combined_len//2)
            return (sorted_list[mid-1] + sorted_list[mid])/2.0
        else:
            mid = (combined_len//2)
            return sorted_list[mid]
       
        