class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balon_count = {"b":0,"a":0,"l":0,"o":0,"n":0}
       
        for t in text:
            if t in balon_count:
                balon_count[t] += 1
                
                
        balon_count['l'] //= 2
        balon_count['o'] //= 2
        
        return min(balon_count.values())
        
        