class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq = Counter(arr)
        heap = list(freq.values())
        heapify(heap)
        
        deletion = 0
        while heap:
            deletion += heap[0]
            if deletion > k:
                break
                
            heappop(heap)
            
        return len(heap)
        