class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = {}
        l = 0
        longest = 0
        
        for r in range(len(s)):
            while s[r] in window:
                
                if window[s[l]] > 1:
                    window[s[l]] -= 1
                else:
                    del window[s[l]]
                l += 1
            window[s[r]] = window.get(s[r],0)+1
            longest = max(longest,r-l+1)
            
        return longest
                
        