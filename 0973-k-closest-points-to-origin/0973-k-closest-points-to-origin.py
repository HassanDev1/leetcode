class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        heap = []
        for x,y in points:
            dist = x**2 + y**2
            heappush(heap,(dist,[x,y]))
          
                
                
        res = []
        for i in range(k):
            item = heappop(heap)
            res.append(item[1])
            
        return res