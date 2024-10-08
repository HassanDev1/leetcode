class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        fleets = []
        for p,s in zip(position,speed):
            fleets.append((p,(target - p)/s))
            
        fleets.sort(reverse=True)   
        for _,t in fleets:
            while not stack or stack[-1] < t:
                stack.append(t)
        
        return len(stack)
        