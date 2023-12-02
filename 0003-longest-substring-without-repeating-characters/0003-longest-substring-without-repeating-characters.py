class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = defaultdict(int)
        l = 0
        longest = 0
        
        for r,c in enumerate(s):
            if c in seen:
                l = max(l,seen[s[r]]+1)
            longest = max(longest,r-l+1)
            seen[c] = r
            
            
            
            
        return longest
        