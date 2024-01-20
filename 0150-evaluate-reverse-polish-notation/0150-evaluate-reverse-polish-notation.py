class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop()+stack.pop())
                
            elif t == "*":
                stack.append(stack.pop()*stack.pop())
                
            elif t == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            elif t == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
                
            else:
                stack.append(int(t))
                
        return stack[-1]
        