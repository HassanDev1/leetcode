class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        heap = []
        for key,v in counter.items():
            heappush(heap,(v,key))
            if len(heap) > k:
                heappop(heap)
                
        print(heap)
        res = []
        for v,key in heap:
            res.append(key)
        return res
        
        