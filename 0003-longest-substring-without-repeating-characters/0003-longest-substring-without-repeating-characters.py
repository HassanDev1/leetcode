class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = defaultdict(int)
        l = 0
        longest = 0
        
        for i in range(len(s)):

            while s[i] in window:
                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                    window[s[l]] -= 1
                l += 1
                
            window[s[i]] =  window.get(s[i],0) + 1
            longest = max(longest,i-l+1)
            
        return longest
                
            