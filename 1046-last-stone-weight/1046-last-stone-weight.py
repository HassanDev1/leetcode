class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        heap = []
        
        for s in stones:
            heappush(heap,-s)
          
        res = []
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            if x != y:
                nw = abs(y-x)
                heappush(heap,-nw)
                
        return -heap[0] if heap else 0