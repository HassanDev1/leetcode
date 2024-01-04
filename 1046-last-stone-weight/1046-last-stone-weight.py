class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        heap = []
        
        for s in stones:
            heappush(heap,-s)
            
        while len(heap) > 1:
            x,y = heappop(heap),heappop(heap)
            if x != y:
                new_w = abs(y - x)
                heappush(heap,-new_w)
                
        return -heap[0] if heap else 0
       
    