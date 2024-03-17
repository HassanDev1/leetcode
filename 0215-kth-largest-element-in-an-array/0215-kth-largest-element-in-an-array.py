class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        heap = []
        for num in nums:
            heappush(heap,-num)
        
        res = []
        while len(heap):
            res.append(heappop(heap))
            if len(res) == k:
                break
                
        return -res[-1]
            
        
            