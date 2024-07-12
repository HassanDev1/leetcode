class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        
        longest = 0
        seen = {}
        
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]]+1)
                
            seen[s[r]] = r
            
            longest = max(r-l+1,longest)
        return longest
        