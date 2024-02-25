class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        window = defaultdict(int)
        
        longest = 0
        
        for r in range(len(s)):
            while s[r] in window:
                
                
                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                    window[s[l]] -= 1
                l += 1
                
            longest = max(longest,r-l+1)
            window[s[r]] += 1
            
        return longest
        