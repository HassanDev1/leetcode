class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        smallest = float(inf)
        
        l = 0
        r = len(nums)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[r] > nums[mid]:
                smallest = min(smallest,nums[mid])
                r = mid-1
            else:
                smallest = min(smallest,nums[mid])
                l = mid+1
                
            
        return smallest
                
        
        