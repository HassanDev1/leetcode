class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def generate(openC,closeC):
            if closeC == openC == n:
                res.append("".join(stack))
                
            if openC < n:
                stack.append("(")
                generate(openC+1,closeC)
                stack.pop()
                
            if closeC < openC:
                stack.append(")")
                generate(openC,closeC+1)
                stack.pop()
                
        generate(0,0)
        return res
                
        