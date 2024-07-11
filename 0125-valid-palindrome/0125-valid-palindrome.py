class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palindrome = []
        
        for c in s:
            if c.isalnum():
                palindrome.append(c.lower())
                
        i,j=0,len(palindrome)-1
        
        while i < j:
            if palindrome[i] != palindrome[j]:
                return False
            i += 1
            j -= 1
            
        return True
        