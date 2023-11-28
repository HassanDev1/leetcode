class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        heap = []
        
        freq = Counter(nums)
        
        for key,val in freq.items():
            heappush(heap,(val,key))
            
            if len(heap) > k:
                heappop(heap)
                
        for ele,val in heap:
            res.append(val)
            
        return res
        