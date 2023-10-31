class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_freq = Counter(t)
        window_s = {}
        min_len = float("inf")
        count = 0
        min_window = ""
        
        left = 0
        for right in range(len(s)):
            if s[right] in t_freq:
                window_s[s[right]] = 1 + window_s.get(s[right],0)
                
                if window_s[s[right]] <= t_freq[s[right]]:
                    count += 1
                
            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right-left + 1
                    min_window = s[left:right+1]
                if s[left] in t_freq:
                    window_s[s[left]] -= 1
                    if window_s[s[left]] < t_freq[s[left]]:
                        count -= 1
                    
                left += 1
        return min_window
        