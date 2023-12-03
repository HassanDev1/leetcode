class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        seen =  Counter(s1)
        window = {}
        
        l = 0
        
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r],0) + 1
            
            if r-l+1 == len(s1):
                if window == seen:
                    return True
                else:
                    if window[s2[l]] == 1:
                        del window[s2[l]]
                    else:
                        window[s2[l]] -= 1
                l += 1
                        
        return False
        
        
        
        