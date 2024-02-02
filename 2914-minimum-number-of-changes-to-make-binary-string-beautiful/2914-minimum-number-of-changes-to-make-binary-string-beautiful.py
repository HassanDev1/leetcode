class Solution:
    def minChanges(self, s: str) -> int:
        
        l = 0
        count = 0
        for r in range(1,len(s),2):
            if s[r] != s[l]:
                count += 1
            l += 2
            
        return count
        