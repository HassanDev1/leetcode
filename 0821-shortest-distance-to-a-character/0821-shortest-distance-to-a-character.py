class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        res = [len(s)]*len(s)
        
        def dfs(i,distance):
            if  i < 0 or i > len(s)-1 or res[i] <= distance:
                return
           
            res[i] = distance
            
            dfs(i+1,distance+1)
            dfs(i-1,distance+1)
            
        for i in range(len(s)):
            if s[i] == c:
                dfs(i,0)
        return res
        