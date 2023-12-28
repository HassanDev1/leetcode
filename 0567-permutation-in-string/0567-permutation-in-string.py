class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        window = {}
        
        l = 0
        if len(s1) > len(s2):
            return False
        
        for r in range(len(s2)):
            
            window[s2[r]] = window.get(s2[r],0)+1
                
            if r-l+1 == len(s1):
                if window == freq:
                    return True
                if window[s2[l]] == 1:
                    del window[s2[l]]
                else:
                    window[s2[l]] -= 1
                l += 1
        return False
        