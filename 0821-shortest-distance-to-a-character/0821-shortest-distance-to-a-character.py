class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')] * n
        pos = float('-inf')

        # Iterate from left to right to find closest occurrence of c
        for i in range(n):
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i], abs(i - pos))

        pos = float('inf')

        # Iterate from right to left to find closest occurrence of c
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i], abs(i - pos))

        return ans
        