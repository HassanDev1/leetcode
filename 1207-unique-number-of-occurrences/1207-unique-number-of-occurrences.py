class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        
        res = set()
        for k,v in freq.items():
            if v in res:
                return False
            res.add(v)
            
        return True
        