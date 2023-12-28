class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq = Counter(t)
        window = {}
        have,need = 0, len(t)
        min_len = float("inf")
        res = ""
        
        l = 0
        
        for r in range(len(s)):
            if s[r] in freq:
                window[s[r]] = window.get(s[r],0) + 1
                if window[s[r]] <= freq[s[r]]:
                    have += 1
                    
            while have == need:
                if r -l + 1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                    
                if s[l] in freq:
                    window[s[l]] -= 1
                    if window[s[l]] < freq[s[l]]:
                        have -= 1
                    
                l += 1
        return res
                    
        