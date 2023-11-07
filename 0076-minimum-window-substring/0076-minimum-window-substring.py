class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        count_t = Counter(t)
        window = {}
        have,need = 0,len(t)
        l = 0
        min_len = float("inf")
        res = ""
        
        for r in range(len(s)):
            if s[r] in count_t:
                window[s[r]] = window.get(s[r],0) +1
                if window[s[r]] <= count_t[s[r]]:
                    have += 1
            while have == need:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                if s[l] in count_t:
                    window[s[l]] -= 1
                    
                    if window[s[l]] < count_t[s[l]]:
                        have -= 1
 
                l += 1
        return res
                    
        