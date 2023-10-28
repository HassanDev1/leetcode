class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        max_len = 0
        l = 0
        
        for r,char in enumerate(s):
            if char in seen:
                l = max(l,seen[char]+1)
            max_len = max(max_len,r-l+1)
            seen[char] = r
        return max_len
            
        