class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq = Counter(arr)
        
        heap = []
        
        for key,val in freq.items():
            heappush(heap,(val,key))
            
            
        deletion_count = 0
        
        for _ in range(len(heap)):
            deletion_count += heap[0][0]
            if deletion_count > k:
                break
            heappop(heap)
            
        return len(heap)