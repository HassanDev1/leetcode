class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        l,r,counter ={},{},Counter(nums)
        
        for i, num in enumerate(nums):
            if num not in l:
                l[num] = i
            r[num] = i
            
        ans = len(nums)
        degree = max(counter.values())
        
        for c in counter:
            if counter[c] == degree:
                ans = min(ans,r[c]-l[c]+1)
                
        return ans
        
        
        