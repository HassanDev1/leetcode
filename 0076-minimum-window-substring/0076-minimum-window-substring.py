class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict = {}
        t_dict = {}

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        left = 0
        min_len = float('inf')
        min_window = ""
        count = 0

        for right in range(len(s)):
            if s[right] in t_dict:
                s_dict[s[right]] = s_dict.get(s[right], 0) + 1
                if s_dict[s[right]] <= t_dict[s[right]]:
                    count += 1

            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]

                if s[left] in t_dict:
                    s_dict[s[left]] -= 1
                    if s_dict[s[left]] < t_dict[s[left]]:
                        count -= 1
                left += 1

        return min_window
        