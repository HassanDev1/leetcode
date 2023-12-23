class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        longest = 0
        
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]]+1)
            longest = max(longest,r-l+1)
            seen[s[r]] = r
            
        return longest
                
            