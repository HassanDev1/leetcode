class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for x,y in points:
            dist = x**2 + y**2
            heappush(heap,(dist,[x,y]))
            
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res