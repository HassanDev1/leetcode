class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        
        for s in stones:
            heappush(heap,-s)
            
        while len(heap)>1:
            x = heappop(heap)
            y = heappop(heap)
            if x != y:
                new_stone = abs(x-y)
                heappush(heap,-new_stone)
                
        return -heap[0] if heap else 0
        
        