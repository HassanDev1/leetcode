class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0]*len(temperatures)
        
        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                l = stack.pop()
                res[l] = r-l

            stack.append(r)
            
        return res
        