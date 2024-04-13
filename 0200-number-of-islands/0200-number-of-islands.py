class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        def helper(r,c):
            q = deque([(r,c)])
            
            while q:
                row,col = q.popleft()
                for i,j in [(row+1,col),(row-1,col),(row,col-1),(row,col+1)]:
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                        grid[i][j] = "0"
                        q.append((i,j))
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    helper(r,c)
                    count += 1
        return count

        