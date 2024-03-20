class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        count_right = 0
        l,r = 0,len(s)-1
        
        while l < r and count_right <=1:
            if s[l] != s[r]:
                count_right += 1
            else:
                r -= 1
            l += 1
        if count_right <= 1:
            return True
        
        count_right = 0
        l,r = 0,len(s)-1
        
        while l < r and count_right <=1:
            if s[l] != s[r]:
                count_right += 1
            else:
                l += 1
            r -= 1
        return count_right <= 1
        