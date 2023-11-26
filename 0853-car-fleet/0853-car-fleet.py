class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet = [(p,(target-p)/s) for p,s in zip(position,speed)]
        
        fleet.sort(key = lambda x:x[0],reverse=True)
        
        stack = []
        
        for p,t in fleet:
            if not stack or stack[-1] < t:
                stack.append(t)
                
        return len(stack)
                
        