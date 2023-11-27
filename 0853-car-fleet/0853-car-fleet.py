class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        fleet = [(p,(target-p)/s) for p,s in zip(position,speed)]
        
        fleet.sort(key=lambda x:x[0], reverse=True)
        
        for p,t in fleet:
            
            while not stack or stack[-1][1] < t:
                stack.append((p,t))
                
                
        return len(stack)
        