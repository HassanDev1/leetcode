class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for op in tokens:
            if op not in "+,-,*,/":
                stack.append(int(op))
            elif op == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif op == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            elif op == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            elif op == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
                
        return stack[-1]
            
        