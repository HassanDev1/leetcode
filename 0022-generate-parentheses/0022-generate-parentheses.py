class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def backtrack(opened_count,closed_count):
            if opened_count == closed_count == n:
                res.append("".join(stack))
                
                
            if opened_count < n:
                stack.append("(")
                backtrack(opened_count+1,closed_count)
                stack.pop()
            if closed_count < opened_count:
                stack.append(")")
                backtrack(opened_count,closed_count+1)
                stack.pop()
        
        backtrack(0,0)
        return res
        