class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        def dfs(i,n,k):
            if i == n:
                if len(temp) == k:
                    res.append(temp.copy())
                return
            
            temp.append(i)
            dfs(i+1,n,k)
            temp.pop()
            dfs(i+1,n,k)
        
        dfs(1,n+1,k)
        return res
            