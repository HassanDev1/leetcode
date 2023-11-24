class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        res = ""
        have,need = 0,len(t)
        l = 0
        min_len = float("inf")
        window = {}
        seen = Counter(t)
        
        for r in range(len(s)):
            if s[r] in seen:
                window[s[r]] = window.get(s[r],0)+1
                
                if window[s[r]] <= seen[s[r]]:
                    have += 1
            while have == need:
                if r -l +1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                if s[l] in seen:
                    window[s[l]] -= 1
                    if window[s[l]] < seen[s[l]]:
                        have -= 1
                    
                l += 1
        return res