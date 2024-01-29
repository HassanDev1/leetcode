class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stack = []
        heap = []
        for s in stones:
            heappush(heap,-s)
            
        while len(heap) > 1:
            s1 = heappop(heap)
            s2 = heappop(heap)
            if s1 != s2:
                val = abs(s2-s1)
                heappush(heap,-val)
                
                
        return -heap[0] if heap else 0
                
       
        