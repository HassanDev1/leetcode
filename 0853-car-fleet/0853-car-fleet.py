class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        
        fleets = [(p,(target-p)/s) for p,s in zip(position,speed)]
        
        fleets.sort(key=lambda x:x[0],reverse=True)
        
        for p,t in fleets:
            while not stack or stack[-1] < t:
                stack.append(t)
                
        return len(stack)
        