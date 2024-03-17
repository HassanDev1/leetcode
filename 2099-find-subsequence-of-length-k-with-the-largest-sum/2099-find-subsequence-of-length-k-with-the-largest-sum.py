class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        
        heap = []
        
        for i,num in enumerate(nums):
            heappush(heap,(num,i))
            
            if len(heap) > k:
                heappop(heap)
        res = []     
        while len(heap):
            res.append(heappop(heap))
            
        res.sort(key=lambda x:x[1])
        
    
        output = []
        for num,_ in res:
            output.append(num)
                
                
        
       
            
        return output