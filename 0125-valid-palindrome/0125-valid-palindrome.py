class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        char  = [c.lower() for c in s if c.isalnum()]
        
        l,r = 0, len(char)-1
        
        while l < r:
            if char[l] != char[r]:
                return False
            l += 1
            r -= 1
        return True
        
        