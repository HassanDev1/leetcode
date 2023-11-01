class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        window = deque()
        res = []
        
        for i in range(len(nums)):
            while window and window[0] < i-k+1:
                window.popleft()
                
            while window and nums[window[-1]] < nums[i]:
                window.pop()
                
            window.append(i)
            
            if i >= k-1:
                res.append(nums[window[0]])
                
        return res
        