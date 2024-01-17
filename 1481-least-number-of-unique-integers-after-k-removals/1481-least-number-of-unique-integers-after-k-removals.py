class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq = Counter(arr)
        heap = []
        for key,val in freq.items():
            heappush(heap,(val,key))
        
        deletion = 0
        
        for _ in range(len(heap)):
            deletion += heap[0][0]
            if deletion > k:
                break
            heappop(heap)
                
        return len(heap)