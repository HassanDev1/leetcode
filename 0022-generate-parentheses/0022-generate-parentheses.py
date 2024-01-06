class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def generate(opCount,clClount):
            if clClount == opCount == n:
                res.append("".join(stack))
                return
            if opCount < n:
                stack.append("(")
                generate(opCount + 1,clClount)
                stack.pop()
            if clClount < opCount:
                stack.append(")")
                generate(opCount,clClount+1)
                stack.pop()
        generate(0,0)
        return res
                
        