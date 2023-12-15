class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_freq = Counter(t)
        s_freq = Counter(s)
        
        return t_freq == s_freq