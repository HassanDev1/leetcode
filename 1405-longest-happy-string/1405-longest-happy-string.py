class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        freq = {"a":a,"b":b,"c":c}
        
        res = []
        heap = []
        for char,count in freq.items():
            if count:
                heappush(heap,(-count,char))
            
        while heap:
            count,char = heappop(heap)
            if len(res)>1 and res[-2] == res[-1] == char:
                if not heap:
                    break
                count2,char2 = heappop(heap)
                count2 += 1
                res.append(char2)
                
                if count2:
                    heappush(heap,(count2,char2))
            
            count += 1
            if count:
                heappush(heap,(count,char))
            res.append(char)
            
        return "".join(res)