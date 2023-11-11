class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        
        heap = []
        res = []
        
        for key,val in freq.items():
            heappush(heap,(val,key))
            
            if len(heap) > k:
                heappop(heap)
                
        for val,key in heap:
            res.append(key)
            
        return res