class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        length = len(s)
      
        # Initialize a 2D array with zeros, where dp[i][j] will hold the length of the longest
        # palindromic subsequence between indices i and j in string s
        dp = [[0] * length for _ in range(length)]
      
        # A single character is always a palindrome of length 1, 
        # so we populate the diagonals with 1
        for i in range(length):
            dp[i][i] = 1
          
        # Loop over pairs of characters from end to start of the string
        for j in range(1, length):
            for i in range(j - 1, -1, -1):
                # If characters at index i and j are the same, they can form a palindrome:
                # - Add 2 to the length of the longest palindromic subsequence we found
                #   between i + 1 and j - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Otherwise, take the maximum of the lengths found by:
                    # - Excluding the j-th character (considering subsequence from i to j - 1)
                    # - Excluding the i-th character (considering subsequence from i + 1 to j)
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                  
        # The entire string's longest palindromic subsequence length is at dp[0][length-1]
        return dp[0][length - 1]