class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def start_from_center(input_str,l,r):
            while l >=0 and r < len(input_str) and input_str[l] == input_str[r]:
                l -= 1
                r += 1
            return input_str[l+1:r]
        
        res = ""
        for i in range(len(s)):
            pal1 = start_from_center(s,i,i)
            if len(pal1) > len(res):
                res = pal1
            pal2 = start_from_center(s,i,i+1)
            if len(pal2) > len(res):
                res = pal2
                
        return res
                    
        