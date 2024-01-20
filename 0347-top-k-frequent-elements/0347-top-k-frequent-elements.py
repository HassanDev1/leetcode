class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        heap = []
        
        for key,val in freq.items():
            heappush(heap,(-val,key))
        
        
        res = []
        for _ in range(k):
            res.append(heap[0][1])
            heappop(heap)
            
        return res
            
            
        