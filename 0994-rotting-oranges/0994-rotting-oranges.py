class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        fresh = set()
        rotten = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        count_min = 0
        
        while rotten and fresh:
            count_min += 1
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                
                for dir in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if dir in fresh:
                        fresh.remove(dir)
                        rotten.append(dir)
                        
        return -1 if fresh else count_min
                    
        