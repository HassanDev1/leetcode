class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balon_freq = {"b":0,"a":0,"l":0,"o":0,"n":0}
        
        for c in text:
            if c in balon_freq:
                balon_freq[c] += 1
                
        balon_freq["l"] //=2
        balon_freq["o"] //=2
        
        return min(balon_freq.values())
        