class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        left = 0
        min_len = float("inf")
        res = ""
        freq = Counter(t)
        window = {}
        have,need = 0,len(t)
        
        for right in range(len(s)):
            if s[right] in freq:
                window[s[right]] = window.get(s[right],0) + 1
                if window[s[right]] <= freq[s[right]]:
                    have += 1
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
                
                if s[left] in freq:
                    window[s[left]] -= 1
                    if window[s[left]] < freq[s[left]]:
                        have -= 1
                            
                left += 1
                
        return res
            
            
        