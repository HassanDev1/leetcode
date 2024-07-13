class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        res = [-1,-1]
        min_len = float("inf")
        window = Counter(t)
        s_freq = {}
        have,need = 0,len(window)
        
        for r in range(len(s)):
            s_freq[s[r]] = s_freq.get(s[r],0) + 1
            
            if s[r] in window and s_freq[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < min_len:
                    res = [l,r]
                    min_len = r-l+1
                    
                s_freq[s[l]] -= 1
                if s[l] in window and s_freq[s[l]] < window[s[l]]:
                    have -= 1
                                                              
                l += 1
        l,r = res
        return s[l:r+1]
        