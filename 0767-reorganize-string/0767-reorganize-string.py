class Solution:
    def reorganizeString(self, s: str) -> str:
        
        res = []
        heap = []
        freq = Counter(s)
        
        for char,count in freq.items():
            if count:
                heappush(heap,(-count,char))
                
                
        prev_count = 0
        prev_char = ""
        
        while heap:
            count,char = heappop(heap)
            
            res.append(char)
            count += 1
            if prev_count != 0:
                heappush(heap,(prev_count,prev_char))
            prev_count = count
            prev_char = char
         
        if len(res) != len(s):
            return ""
        return "".join(res)
            