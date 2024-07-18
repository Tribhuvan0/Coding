class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        count = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    self.dfs(grid,i,j,visited)
                    count += 1
        return count
        
    def dfs(self,grid,i,j,visited):
        if min(i,j) < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1' or (i,j) in visited:
            return
        
        visited.add((i,j))
        self.dfs(grid,i+1,j,visited)
        self.dfs(grid,i-1,j,visited)
        self.dfs(grid,i,j+1,visited)
        self.dfs(grid,i,j-1,visited)
        #visited.remove((i,j))
        
        
            
        