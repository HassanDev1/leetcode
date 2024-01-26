class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for s in stones:
            heappush(heap,-s)
            
        while len(heap) > 1:
            s1 = heappop(heap)
            s2 = heappop(heap)
            
            if s1 != s2:
                new_res = abs(s2-s1)
                heappush(heap,-new_res)
                
        return -heap[0] if heap else 0
                
                