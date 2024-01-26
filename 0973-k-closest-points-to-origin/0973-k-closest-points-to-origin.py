class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        distances = []
        for x,y in points:
            d = x**2 + y**2
            heappush(heap,(-d,[x,y]))
            if len(heap) > k:
                heappop(heap)
                
        res = []
        for items in heap:
            res.append(items[1])
            
        return res