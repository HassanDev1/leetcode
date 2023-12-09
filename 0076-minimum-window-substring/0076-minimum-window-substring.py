class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = ""
        freq = Counter(t)
        l = 0
        
        window = {}
        min_str = float("inf")
        have = 0
        need = len(t)
        
        for r,c in enumerate(s):
            if c in freq:
                window[c] = window.get(c,0)+1
                if window[c] <= freq[c]:
                    have += 1
            while have == need:
                if r-l+1 < min_str:
                    min_str = r-l+1
                    res = s[l:r+1]
                    
                if s[l] in freq:
                    window[s[l]] -= 1
                    if window[s[l]] < freq[s[l]]:
                        have -= 1
                    
                l += 1
        return res
                
        