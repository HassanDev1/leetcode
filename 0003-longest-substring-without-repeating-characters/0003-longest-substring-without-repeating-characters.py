class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window_start = 0
        max_len = 0
        hmap = {}
        
        for end in range(len(s)):
            right = s[end]
            
            if right in hmap:
                window_start = max (window_start,hmap[right] + 1)
            hmap[right] = end
            
            max_len = max(max_len,end-window_start + 1)
            
        return max_len
        