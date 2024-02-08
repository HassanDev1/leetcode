class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        count = Counter(nums)
        for ele,freq in count.items():
            heappush(heap,(-freq,ele))
           
            
            
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
            
        return res
        
            