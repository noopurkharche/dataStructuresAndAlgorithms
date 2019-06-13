def dfs(grid, x, y, count):
    
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or grid[x][y] == -1:
        return float("inf")
    
    if grid[x][y] == 9:
        return count
    
    
    temp = grid[x][y]
    grid[x][y] = -1
    v1 = dfs(grid, x + 1, y, count + 1)
    v2 = dfs(grid, x - 1, y, count + 1)
    v3 = dfs(grid, x, y + 1, count + 1)
    v4 = dfs(grid, x, y - 1, count + 1)
    grid[x][y] = temp
    
    return min(v1,v2,v3,v4)
    


grid = [[1,0,9,0],
        [1,1,1,1],
        [0,1,0,0],
        [1,1,1,1]]
        
print(dfs(grid, 0, 0, 0))
