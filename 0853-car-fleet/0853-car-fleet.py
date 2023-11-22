class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        fleet = []
        for p,s in zip(position,speed):
            time = (target-p)/s
            fleet.append((p,time))
            
        fleet.sort(key=lambda x:x[0],reverse=True)
        
        for _,t in fleet:
            if not stack or stack[-1] < t:
                stack.append(t)
                
        return len(stack)
        