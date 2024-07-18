class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    perimeter += self.dfs(grid,r,c,visited)
                    return perimeter
        
        return perimeter
    
    def dfs(self,grid,r,c,visited):
        if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] != 1:
            return 1
        if (r,c) in visited:
            return 0
        visited.add((r,c))
        perimeter = 0
        perimeter += self.dfs(grid,r+1,c,visited)
        perimeter += self.dfs(grid,r-1,c,visited)
        perimeter += self.dfs(grid,r,c+1,visited)
        perimeter += self.dfs(grid,r,c-1,visited)
        
        return perimeter
        