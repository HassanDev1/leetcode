class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq_word = Counter(s)
        heap = []
        for k,v in freq_word.items():
            heappush(heap,(-v,k))
            
        res = []
        prev_count,prev_char = 0,""
        while heap:
            freq,char = heappop(heap)
            res.append(char)
            
            if prev_count < 0:
                heappush(heap,(prev_count,prev_char))
                
            freq += 1
            prev_count,prev_char = freq,char
             
            
        if len(res) != len(s):
            return ""
        return "".join(res)
            
        