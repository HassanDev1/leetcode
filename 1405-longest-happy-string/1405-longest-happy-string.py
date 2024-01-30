class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        freq = {}
        for count,char in [(a,"a"),(b,"b"),(c,"c")]:
            freq[char] = count
            
        heap = []
        for k,v in freq.items():
            if v:
                heappush(heap,(-v,k))
            
        res = []
        
        while heap:
            count,char = heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                count2,char2 = heappop(heap)
                res.append(char2)
                count2 += 1
                if count2:
                    heappush(heap,(count2,char2))
                   
            res.append(char)
            count += 1
            if count:
                heappush(heap,(count,char))
                
        return "".join(res)
        