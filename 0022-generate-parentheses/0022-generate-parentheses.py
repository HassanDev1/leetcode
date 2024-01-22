class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        stack = []
        res = []
        
        def dfs(count_opened,count_closed):
            if count_opened == count_closed == n:
                res.append("".join(stack))
                return
            
            if count_closed < count_opened:
                stack.append(")")
                dfs(count_opened,count_closed+1)
                stack.pop()
            if count_opened < n:
                stack.append("(")
                dfs(count_opened+1,count_closed)
                stack.pop()
        dfs(0,0)
        return res
        