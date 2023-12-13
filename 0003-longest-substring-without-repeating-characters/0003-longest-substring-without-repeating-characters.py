class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        
        l = 0
        seen = {}
        
        for r,c in enumerate(s):
            if c in seen:
                l = max(l,seen[c]+1)
            longest = max(longest,r-l+1)
            seen[c] = r
        return longest
        
        