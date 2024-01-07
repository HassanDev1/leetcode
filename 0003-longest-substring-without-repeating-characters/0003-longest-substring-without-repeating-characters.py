class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = defaultdict(int)
        longest = 0
        l = 0
        for r,c in enumerate(s):
            if c in seen:
                l = max(seen[c]+1,l)
            longest = max(r-l+1,longest)
            seen[c] = r
        return longest
        