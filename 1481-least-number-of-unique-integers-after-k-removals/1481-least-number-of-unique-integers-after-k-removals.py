class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq = Counter(arr)
        heap = []
        
        for num,count in freq.items():
            heappush(heap,(count))
            
        deletion = 0
        while heap:
            deletion += heap[0]
            if deletion > k:
                break
            heappop(heap)
            
        return len(heap)
        