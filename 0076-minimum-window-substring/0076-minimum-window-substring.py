class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_len = float("inf")
        l = 0
        window = Counter(t)
        
        have = 0
        need = len(t)
        freq = {}
        res = ""
        
        for r in range(len(s)) :
            if s[r] in window:
                freq[s[r]] = freq.get(s[r],0) + 1
                if freq[s[r]] <= window[s[r]]:
                    have += 1
            while have == need:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                if s[l] in window:
                    freq[s[l]] -= 1
                    if freq[s[l]] < window[s[l]]:
                        have -= 1
                        
                l += 1
        return res
        