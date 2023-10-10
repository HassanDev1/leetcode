class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        l = 0
        
        res = [-1,-1]
        min_len = float("inf")
        count_t = Counter(t)
        window = {}
        have,need = 0,len(count_t)
        
        for r in range(len(s)):
            
            c = s[r]
            window[c] = 1 + window.get(c,0)
            
            if c in count_t and window[c] == count_t[c]:
                have += 1
            while have  == need:
                if r-l+1 < min_len:
                    min_len = r - l +1
                    res = [l,r]
                    
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                
                
                l += 1
        l,r = res
        return s[l:r+1]
            
            
        