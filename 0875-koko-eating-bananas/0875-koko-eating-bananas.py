class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def is_possible(mid)->bool:
            total = 0
            
            for pile in piles:
                total += math.ceil(pile/mid)
            if total > h:
                return False
            return True
        
        
        
        l,r = 1,max(piles)
        
        while l < r:
            mid = l +(r-l)//2
            
            if is_possible(mid):
                r = mid
            else:
                l = mid + 1
                
        return l
        