class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        count = Counter(arr)
        heap = []
        for key,val in count.items():
            heappush(heap,val)
            
        deletion = 0    
        for i in range(len(heap)):
            deletion += heap[0]
            if deletion > k:
                break
            heappop(heap)
       
        
        return len(heap)
            