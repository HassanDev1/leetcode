class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq = Counter(nums)
        
        for key,val in freq.items():
            heappush(heap,(val,key))
            
            if len(heap) > k :
                heappop(heap)
        res = []
        for val,key in heap:
            res.append(key)
            
        return res
            
        
        