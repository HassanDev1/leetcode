class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        
        s_map = Counter(s)
        
        for c in t:
            if c in s_map:
                s_map[c] -= 1
                
        for k,v in s_map.items():
            if v > 0:
                return False
            
        return True
        
        