class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = Counter(s)
        count_t = Counter(t)
        
        for c in s:
            if c in count_t:
                count_t[c] -= 1
                
        print(count_t)
        for v in count_t.values():
            
            if v != 0:
                return False
        return True
        
        