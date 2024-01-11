class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        heap = []
        
        count = Counter(arr)
        
        deletion = 0
        heap = []
        
        for m,v in count.items():
            heappush(heap,(v,m))
            
        for i in range(len(heap)):
            deletion += heap[0][0]
            if deletion > k:
                break
            heappop(heap)
                
        return len(heap)
            
            
            
            
            