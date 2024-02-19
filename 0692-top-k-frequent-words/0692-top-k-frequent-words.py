class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = Counter(words)
        
        heap = []
        
        for word,count in freq.items():
            heappush(heap,(-count,word))
          
                
        res = []
        while heap:
            item = heappop(heap)
            res.append(item[1])
            if len(res) >=k:
                break
            
        return res