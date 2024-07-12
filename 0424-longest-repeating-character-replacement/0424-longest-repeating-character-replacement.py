class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        window = {}
        
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            
            while r-l+1 - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            longest = max(longest,r-l+1)
            
        return longest
        
        
        