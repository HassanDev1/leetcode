class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])
        
        l = 0
        for r in range(len(s1),len(s2)):
            if count_s1 == count_s2:
                return True
            count_s2[s2[r]] += 1
            
            if r -l >= len(s1):
                if count_s2[s2[l]] == 1:
                    del count_s2[s2[l]]
                else:
                    count_s2[s2[l]] -= 1
                
                l += 1
                
        return count_s1 == count_s2
        