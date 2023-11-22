class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        
        for t in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[t]:
                j = stack.pop()
                res[j] = t-j
                
            stack.append(t)
        return res
            
        