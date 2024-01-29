class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        window = {}
        l = 0
        for i in range(len(s)):
            
            if s[i] in window:
                l = max(l,window[s[i]]+1)
            
            longest = max(longest,i-l+1)
            window[s[i]] = i
            
        return longest