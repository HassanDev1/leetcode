class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row,col,visited):
            if  row < 0 or row > len(grid)-1 or col <0 or col > len(grid[0])-1 or grid[row][col] == "0" or (row,col) in visited:
                return
            
            visited.add((row,col))
            dfs(row-1,col,visited)
            dfs(row+1,col,visited)
            dfs(row,col-1,visited)
            dfs(row,col+1,visited)
        
        
        count = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c,visited)
                    count += 1
        return count