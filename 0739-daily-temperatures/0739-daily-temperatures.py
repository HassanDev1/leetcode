class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        stack = []
        res = [0]*len(temperatures)
        
        for i,t in enumerate(temperatures):
            
            while stack and stack[-1][1] < t:
                prev_index,_ = stack.pop()
                res[prev_index] = i-prev_index
                
                
            stack.append((i,t))
        return res