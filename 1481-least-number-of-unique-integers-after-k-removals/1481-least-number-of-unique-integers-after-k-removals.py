class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        count = Counter(arr)
        
        heap = []
        
        for key,val in count.items():
            heappush(heap,(val,key))
            
        count_del = 0
        for _ in range(len(heap)):
            count_del += heap[0][0]
            if count_del > k:
                break
            heappop(heap)
            
        return len(heap)