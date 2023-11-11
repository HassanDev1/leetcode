class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = Counter(s1)
        window = {}
        l = 0
        
        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i],0) + 1
            
            if i - l+1 >= len(s1):
                if window == s1_freq:
                    return True
                else:
                    if window[s2[l]] == 1:
                        del window[s2[l]]
                    else:
                        window[s2[l]] -= 1
                l += 1
                        
        return False
                
            
        
        
        