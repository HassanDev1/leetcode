class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for c in tokens:
            
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif c == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                res = int(n2/n1)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[-1]
        