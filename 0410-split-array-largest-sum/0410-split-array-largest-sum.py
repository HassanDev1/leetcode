class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def feasible(threshold):
            tot = 0
            count = 1
            for num in nums:
                tot += num
                if tot > threshold:
                    tot = num
                    count += 1
                    if count > k:
                        return False
            return True
        
        l,r = max(nums),sum(nums)
        while l < r:
            mid = l +(r-l)//2
            
            if feasible(mid):
                r = mid
            else:
                l = mid +1
                
        return l
        