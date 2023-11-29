class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def found(mid):
            if nums[mid] >= target:
                return True
            return False
        
        l,r = 0,len(nums)
        
        while l < r:
            mid = l + (r-l)//2
            
            if found(mid):
                r = mid
            else:
                l = mid+1
        return l
                
        