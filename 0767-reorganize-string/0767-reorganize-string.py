class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = Counter(s)
        
        heap = []
        for char,count in freq.items():
            heappush(heap,(-count,char))
            
        res = []
        prev_char = ""
        prev_count = 0
        while heap:
            count,char = heappop(heap)
            res.append(char)
            if prev_count:
                heappush(heap,(prev_count,prev_char))
            
            count += 1
            prev_count = count
            prev_char = char
            
        if len(res) != len(s):
            return ""
        return "".join(res)
        