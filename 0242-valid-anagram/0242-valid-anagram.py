class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        
        l=0
        for r in range(len(s_sorted)):
            if s_sorted[r] != t_sorted[l]:
                return False
            l += 1
            
        return True
        