class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        
        window = Counter(s1)
        found = {}
        l = 0
        
        for r in range(len(s2)):
            if s2[r] in window:
                found[s2[r]] = found.get(s2[r],0) + 1
                
            if r-l+1 == len(s1):
                if window == found:
                    return True
                if s2[l] in window:
                    if found[s2[l]] <= 1:
                        del found[s2[l]]
                    else:
                        found[s2[l]] -= 1
                        
                l += 1
        return False
            
            