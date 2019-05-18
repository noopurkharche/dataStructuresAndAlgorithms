# Rotate nxn matrix

# method to print the matrix
def printMatrix(matrix):
    n = len(matrix)
    for i in range(0,n):
        temp = ""
        for j in range(0,n):
            temp = temp + " " + str(matrix[i][j])
        print(temp)

# method to rotate the matrix
def rotateImage(matrix):
    row = len(matrix)
    col = row
    numberofLevels = row /2
    level = 0
    last = row -1
    while level < numberofLevels:
        for i in range(level, last):
            matrix[level][i], matrix[i][last] = matrix[i][last], matrix[level][i]
            matrix[level][i], matrix[last][last - i + level] = matrix[last][last - i + level], matrix[level][i]
            matrix[level][i], matrix[last - i + level][level] = matrix[last - i + level][level], matrix[level][i]
        level = level + 1
        last = last - 1

# test case 1
matrix = [[1,2,3], [4,5,6], [7,8,9]]

# test case 2
# matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]] 

print("----------------------Original Matrix -------------------------------")
printMatrix(matrix)

rotateImage(matrix) 
print("----------------------Rotated Matrix -------------------------------")
printMatrix(matrix)
