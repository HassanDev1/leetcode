class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        
        freq = Counter(nums)
        
        for ele,count in freq.items():
            heappush(heap,(-count,ele))
            
        res = []
        while len(heap):
            item = heappop(heap)
            res.append(item[1])
            if len(res) == k:
                break
                
        return res
                
                