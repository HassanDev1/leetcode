class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
        
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                
                output[j] = i -j   #[1,1,4,2,1,1,0,0]
                                   # 0,1,2,3,4,5,6,7  
            stack.append(i)        #[6,7]
        return output
            
        