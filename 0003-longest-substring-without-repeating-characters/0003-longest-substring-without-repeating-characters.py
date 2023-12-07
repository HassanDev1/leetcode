class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        l = 0
        window = {}
        longest = 0
        
        for r in range(len(s)):
            if s[r] in window:
                l = max(l,window[s[r]]+1)
                
            longest = max(longest,r-l+1)
                
            window[s[r]] = r
            
        return longest
        