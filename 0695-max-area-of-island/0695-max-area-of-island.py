class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, self.dfs(grid,r,c,visited))
                    
        return area
    
    def dfs(self,grid,r,c,visited):
        if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in visited or grid[r][c] == 0:
            return 0
        
        visited.add((r,c))
        return (1 +
                self.dfs(grid,r+1,c,visited) +
                self.dfs(grid,r-1,c,visited) +
                self.dfs(grid,r,c+1,visited) + 
                self.dfs(grid,r,c-1,visited) 
               )
        
        