class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        curr_max = max(nums[:k])
        l = 0
        heap = []
        for i in range(0,k):
            heappush(heap,(-nums[i],i))
            
        res.append(heap[0][0])
        for i in range(k,len(nums)):
            
            while heap and heap[0][1] <= i-k:
                heappop(heap)
            
            heappush(heap,(-nums[i],i))
            res.append(heap[0][0])
            
       
        for i in range(len(res)):
            res[i] = -1*res[i]
        return res
        
        
      
        