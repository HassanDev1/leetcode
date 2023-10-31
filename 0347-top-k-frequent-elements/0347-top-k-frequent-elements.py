class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        
        heap = []
        for key,val in freq.items():
            heappush(heap,(val,key))
            
            if len(heap) > k:
                heappop(heap)
                
        res = []
        
        
        for key,val in heap:
            res.append(val)
            
        return res