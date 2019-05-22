
# depth first traversal
def dfs(i,j,m,n,matrix):
    
    # check for bounds or value not equal to 1
    if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] != 1:
        return
    
    # mark the cell as visited
    matrix[i][j] = -1
    dfs(i + 1, j, m, n, matrix)
    dfs(i - 1, j, m, n, matrix)
    dfs(i, j + 1, m, n, matrix)
    dfs(i ,j - 1, m, n, matrix)
    
matrix = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 1, 1]]

m = len(matrix)
n = len(matrix[0])

count = 0

# check for islands starting from every point in the matrix
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1:
            dfs(i,j,m,n,matrix)
            count = count + 1

print("Number of Islands - " + str(count))
