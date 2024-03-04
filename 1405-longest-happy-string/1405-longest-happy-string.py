class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        freq = {"a":a,"b":b,"c":c}
        heap = []
        
        for char,count in freq.items():
            if count:
                heappush(heap,(-count,char))
                
        res = []
        
        prev_count = 0
        prev_char = ""
        
        while len(heap):
            count,char = heappop(heap)
            
                
            if len(res)> 1 and res[-1] == res[-2] == char:
                
                if not heap:
                    break
                count2,char2 = heappop(heap)
                res.append(char2)
                count2 += 1
                if count2:
                    heappush(heap,(count2,char2))
                
            count += 1
            if count:
                heappush(heap,(count,char))
            res.append(char)
        return "".join(res)