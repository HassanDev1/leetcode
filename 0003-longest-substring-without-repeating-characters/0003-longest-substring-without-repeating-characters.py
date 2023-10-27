class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        l = 0
        longest = 0
        
        for r,char in enumerate(s):
            if char in seen:
                l = max(l,seen[char]+1)
                
            longest = max(longest,r -l +1)
            seen[char] = r
            
        return longest
        
    
        
        