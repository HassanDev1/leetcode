class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return False
            i += 1
            j += 1
        return True
        