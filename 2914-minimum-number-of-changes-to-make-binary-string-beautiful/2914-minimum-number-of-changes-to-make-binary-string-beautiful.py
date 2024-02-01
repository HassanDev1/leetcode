class Solution:
    def minChanges(self, s: str) -> int:
        
        res = 0
        l =0
        for r in range(1,len(s),2) :
            if s[l] != s[r]:
                res += 1
            l += 2
        return res
            
        