class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        
        freq = {"b":0,"l":0,"o":0,"n":0}
        
        for t in text:
            if t in freq:
                freq[t] += 1
                
        freq["l"] //= 2
        freq["o"] //= 2
        
        return min(freq.values())