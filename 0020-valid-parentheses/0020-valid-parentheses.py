class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if stack:
                    popped=  stack.pop()
                    if popped == "(" and c != ")" or popped == "[" and c != "]" or popped == "{" and c != "}":
                        return False
                elif not stack and c in ")]}":
                    return False
                    
        return len(stack) == 0
                
        