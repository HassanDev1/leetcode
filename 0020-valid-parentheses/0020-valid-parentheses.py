class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:
            if c in "([{":
                stack.append(c)
            elif not stack and c in ")]}":
                return False
            else:
                if stack and stack[-1] != "(" and c ==")"  or c =="]" and stack[-1] != "[" or c =="}" and stack[-1] != "{": 
                    return False
                else:
                    stack.pop()
                    
        return len(stack) == 0
        