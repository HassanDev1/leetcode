class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(count_op,count_cl):
            if count_op == count_cl == n:
                res.append("".join(stack))
                return
            if count_op < n:
                stack.append("(")
                dfs(count_op+1,count_cl)
                stack.pop()
            if count_cl < count_op:
                stack.append(")")
                dfs(count_op,count_cl+1)
                stack.pop()
            
        dfs(0,0)
        return res