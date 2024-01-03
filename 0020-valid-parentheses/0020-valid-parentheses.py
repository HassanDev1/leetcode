class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}" and not stack:
                return False
            else:
                if stack and c == ")" and stack[-1] != "(" or c == "}" and stack[-1] != "{" or c == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        return not stack
        