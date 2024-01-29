class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        freq = Counter(words)
        heap = []
        
        for key,val in freq.items():
            heappush(heap,(-val,key))
            
        res = []
        for _ in range(k):
            item = heappop(heap)
            res.append(item[1])
            
        return res