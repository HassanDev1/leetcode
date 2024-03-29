class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        freq = {"a":a,"b":b,"c":c}
        
        heap = []
        for char,count in freq.items():
            if count:
                heappush(heap,(-count,char))
                
        res = []
        
        prev_count,prev_char = 0,""
        while heap:
            count,char = heappop(heap)
            
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                count2,char2 = heappop(heap)
                
                count2 += 1
                if count2:
                    heappush(heap,(count2,char2))
                res.append(char2)
            
            count += 1
            res.append(char)
            if count:
                heappush(heap,(count,char))
                
        return "".join(res)
            
            
        