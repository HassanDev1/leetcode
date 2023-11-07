class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        hmap = {}
        
        l = 0
        for r in range(len(s)):
            if s[r] in hmap:
                l = max(l,hmap[s[r]]+1)
            longest = max(longest,r-l+1)
            hmap[s[r]] = r
            
        return longest
            
            