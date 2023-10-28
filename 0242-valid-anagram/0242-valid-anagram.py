class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        
        count_s = Counter(s)
        
        for c in t:
            if c in count_s:
                count_s[c] -= 1
                
        for k,v in count_s.items():
            if v != 0:
                return False
            
        return True
        