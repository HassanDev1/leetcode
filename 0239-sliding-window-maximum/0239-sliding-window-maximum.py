class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()
        res = []
        
        for r,num in enumerate(nums):
            
            while q and q[0] < r-k+1:
                q.popleft()
            
            while q and nums[q[-1]] < num:
                q.pop()
                
            q.append(r)
            if r >= k-1:
                res.append(nums[q[0]])
                
        return res
            
        