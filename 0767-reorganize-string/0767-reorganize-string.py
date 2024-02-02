class Solution:
    def reorganizeString(self, s: str) -> str:
        
        
        freq = Counter(s)
        heap = []
        for char,count in freq.items():
            heappush(heap,(-count,char))
            
        res = []
        prev_count = 0
        prev_char = ""
        
        while heap:
            count,char = heappop(heap)
            
            res.append(char)
            if prev_count < 0:
                heappush(heap,(prev_count,prev_char))
                
            count += 1
            prev_count,prev_char = count,char
            
        if len(res) != len(s):
            return ""
        return "".join(res)