class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        def helper(i):
            if i > len(logs)-1:
                return
            if logs[i] == "./":
                pass
            elif logs[i] == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(logs[i])
                
            helper(i+1)
        helper(0)
        return len(stack)
        