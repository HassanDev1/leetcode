class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        j = 0
        for p in pushed:
            stack.append(p)
            
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                
        return not stack