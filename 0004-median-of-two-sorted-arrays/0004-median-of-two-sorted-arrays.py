class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1+nums2)

        n = len(sorted_nums)
        median = 0

        if n % 2 == 0:
          mid = n//2
          median = (sorted_nums[mid-1] + sorted_nums[mid]) / 2.0
        else:
          mid = n //2
          median = sorted_nums[mid]

        return median
        