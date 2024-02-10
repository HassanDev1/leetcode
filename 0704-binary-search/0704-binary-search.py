class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)
        
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
                
        return -1
        