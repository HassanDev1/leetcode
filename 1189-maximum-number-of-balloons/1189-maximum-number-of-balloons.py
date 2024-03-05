class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {"b":0,"a":0,"l":0,"o":0,"n":0}
        
        for c in text:
            if c in freq:
                freq[c] += 1
            
        freq["l"] //= 2
        freq["o"] //= 2
        return min(freq.values())