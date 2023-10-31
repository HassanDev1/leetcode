class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_window = ""
        min_len = float("inf")
        l = 0
        count = 0
        
        t_dict = Counter(t)
        s_dict = {}
        
        for r in range(len(s)):
            if s[r] in t_dict:
                s_dict[s[r]] = s_dict.get(s[r],0) + 1
                if s_dict[s[r]] <= t_dict[s[r]]:
                    count += 1
            while count == len(t):
                if r -l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                #shrink my window
                if s[l] in t_dict:
                    s_dict[s[l]] -= 1
                    if s_dict[s[l]] < t_dict[s[l]]:
                        count -= 1
                l += 1
        return min_window
        
        