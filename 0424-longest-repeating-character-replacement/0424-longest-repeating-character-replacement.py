class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        freq = defaultdict()
        max_len = 0
        
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            
            while r-l+1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(r-l+1, max_len)
            
        return max_len
        
        