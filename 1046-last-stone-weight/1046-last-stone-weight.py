class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for stone in stones:
            heappush(heap,-stone)
            
        while len(heap) > 1:
            val1 = heappop(heap)
            val2 = heappop(heap)
            if val1 != val2:
                new_stone = abs(val1-val2)
                heappush(heap,-new_stone)
                
                
        return -heap[0] if heap else 0
                
            