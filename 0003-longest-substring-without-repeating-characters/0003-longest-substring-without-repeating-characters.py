class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        l = 0
        
        seen = {}
        
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]]+1)
            longest = max(r-l+1,longest)
            seen[s[r]] = r
            
                
        return longest
        