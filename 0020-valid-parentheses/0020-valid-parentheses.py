class Solution:
    def isValid(self, s: str) -> bool:
        
        store = {"(":")","[":"]","{":"}"}
        
        
        stack = []
        
        for c in s:
            if c in "([{":
                stack.append(c)
                
            else:
                if not stack or store[stack[-1]] != c:
                    return False
                else:
                    if stack:
                        stack.pop()
                        
        return len(stack) == 0