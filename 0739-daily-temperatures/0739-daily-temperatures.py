class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0]*len(temperatures)
    
        
        for d in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[d]:
                j = stack.pop()
                res[j] = d-j  
                
                
            stack.append(d)
          
            
        return res
                
        