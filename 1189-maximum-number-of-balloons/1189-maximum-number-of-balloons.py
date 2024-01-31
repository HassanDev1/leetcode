class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_count = Counter({key:0 for key in "balon"})
        
        for char in text:
            if char in balloon_count:
                balloon_count[char] += 1
            
        balloon_count["l"] //=2
        balloon_count["o"] //= 2
        
        return min(balloon_count.values())
                                
                                
                    