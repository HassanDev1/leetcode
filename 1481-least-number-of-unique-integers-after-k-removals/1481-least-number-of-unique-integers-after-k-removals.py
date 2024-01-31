class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        count = Counter(arr)
        
        heap = []
        for num,freq in count.items():
            heappush(heap,(freq))
            
        deletion = 0
        
        while heap:
            deletion += heap[0]
            if deletion > k:
                break
            heappop(heap)
                
        return len(heap)