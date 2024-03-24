class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(op,cl,temp):
            if op == cl == n:
                res.append("".join(temp))
                return
            if cl < op:
                temp.append(")")
                helper(op,cl+1,temp)
                temp.pop()
            if op < n:
                temp.append("(")
                helper(op+1,cl,temp)
                temp.pop()
        helper(0,0,[])
        return res
                
        
                
        