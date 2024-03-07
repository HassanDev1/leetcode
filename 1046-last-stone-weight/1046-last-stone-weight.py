class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for s in stones:
            heappush(heap,-s)
            
            
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            if x != y:
                diff = abs(x-y)
                heappush(heap,-diff)
                
        return -heap[0] if heap else 0
        
        