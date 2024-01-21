class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        seen = Counter(s1)
        
        window = {}
        l = 0
        if len(s1) > len(s2):
            return False
        
        for r,c in enumerate(s2):
            
            window[c] = window.get(c,0)+1
            if r-l+1 >= len(s1):
                if window == seen:
                    return True
                else:
                    if window[s2[l]] == 1:
                        del window[s2[l]]
                    else:
                        window[s2[l]] -= 1
                        
                l += 1
                
        return False
            