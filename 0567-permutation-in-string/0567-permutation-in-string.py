class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        have = Counter(s1)
        need =  {}
        
        l = 0
        
        for r in range(len(s2)):
            need[s2[r]] = 1 + need.get(s2[r],0)
            
            if r -l +1 == len(s1):
                
                if need == have:
                    return True
                else:
                    if need[s2[l]] == 1:
                        del need[s2[l]]
                    else:
                        need[s2[l]] -= 1
                l += 1
                
        return False
        
        
        
        
        