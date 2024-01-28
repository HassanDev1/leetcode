class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = Counter(s)
        heap = []
        for char,count in freq.items():
            if count != 0:
                heappush(heap,(-count,char))
                
        prev_freq,prev_char = 0,""
        res = []
        while heap:
            count,char = heappop(heap)
            
            res.append(char)
            if prev_freq < 0:
                heappush(heap,(prev_freq,prev_char))
            
            count += 1
            prev_freq = count
            prev_char = char
            
        if len(res) != len(s):
            return ""
        return "".join(res)
        
            
        