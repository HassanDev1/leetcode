class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        heap = []
        
        for key,v in count.items():
            heappush(heap,(v,key))
            while len(heap)> k:
                heappop(heap)
            
       
        res = []
        for i in range(k):
            res.append(heap[i][1])
        return res
            
        
            
            
        
        
        