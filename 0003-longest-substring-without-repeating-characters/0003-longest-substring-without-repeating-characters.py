class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        seen = {}
        
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]]+1,l)
                
            longest = max(r-l+1,longest)
            seen[s[r]] = r
            
        return longest        