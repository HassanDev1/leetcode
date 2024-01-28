class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count,char in [(a,"a"),(b,"b"),(c,"c")]:
            if count != 0:
                heappush(heap,(-count,char))
                
        res = []      
        while heap:
            count,char = heappop(heap)
            
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                count1,char1 = heappop(heap)
                count1 += 1
                res.append(char1)
                if count1:
                    heappush(heap,(count1,char1))
                    
            else:
                res.append(char)
                count += 1
            if count:
                heappush(heap,(count,char))
                
        return "".join(res)
                
            
            
        