class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        heap = []
        
        count = Counter(arr)
        
        
        
        for m,v in count.items():
            heappush(heap,(v,m))
            
        deletion = 0
            
        for _ in range(len(heap)):
            deletion += heap[0][0]
            if deletion > k:
                break
            heappop(heap)
            
                
        return len(heap)