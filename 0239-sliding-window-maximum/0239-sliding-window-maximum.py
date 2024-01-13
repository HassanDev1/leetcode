class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        
        res = []
        q = deque()
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)
            if r - q[0] + 1 > k:
                q.popleft()
    
            if r >= k-1:
                res.append(nums[q[0]])
                
        return res
        