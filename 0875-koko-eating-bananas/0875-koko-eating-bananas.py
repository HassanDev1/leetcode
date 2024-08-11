class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasible(mid):
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid)
            if total <= h:
                return True
            return False
            
        l=1
        r = max(piles)
        
        while l < r:
            mid = l + (r-l)//2
            
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
                
        if feasible(l) <= h:
            return l
        else:
            return r
                