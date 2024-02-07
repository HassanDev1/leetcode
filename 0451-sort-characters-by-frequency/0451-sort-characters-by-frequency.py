class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        
        heap = []
        freq = Counter(s)
        for char,count in freq.items():
            heappush(heap,(-count,char))
            
        while heap:
            count,char = heappop(heap)
            
            for _ in range(-count):
                res.append(char)
                
        return "".join(res)
        