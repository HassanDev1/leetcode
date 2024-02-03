class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def compare(mid):
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            if total > h:
                return True
            return False
        
        l,r = 1,max(piles)
        while l < r:
            mid = l + (r-l)//2
            
            if compare(mid):
                l = mid + 1
            else:
                r = mid
        return l