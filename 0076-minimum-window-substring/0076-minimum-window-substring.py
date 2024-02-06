class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        window = {}
        l = 0
        res = ""
        min_len = float("inf")
        have,need = 0, len(t)
        
        for r in range(len(s)):
            if s[r] in t_map:
                window[s[r]] = window.get(s[r],0)+1
                if window[s[r]] <= t_map[s[r]]:
                    have += 1
                    
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                    
               
                if s[l] in t_map:
                    window[s[l]] -= 1
                    if window[s[l]] < t_map[s[l]]:
                        have -= 1
                l += 1
        return res