class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        
        for i,ele in enumerate(temperatures):
            while stack and stack[-1][1] < ele:
                prev_ind,_ = stack.pop()
                res[prev_ind] = i - prev_ind
            stack.append((i,ele))
            
        return res
        