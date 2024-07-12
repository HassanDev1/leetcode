class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
       
        longest = 0
        seen = {}
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]]+1)
                del seen[s[r]]
                
                
            seen[s[r]] = r
            longest = max(r-l+1,longest)
        return longest
        
        
        