class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = [0]
        
        def helper(i):
            if i >= len(logs):
                return
            if logs[i] == "./":
                pass
            elif logs[i] == "../":
                if depth[0] > 0:
                    depth[0] -= 1
            else:
                depth[0] += 1
                
            helper(i+1)
        helper(0)
        return depth[0]
        