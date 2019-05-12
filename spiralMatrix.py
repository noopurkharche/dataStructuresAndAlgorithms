# this method prints the give matrix in spiral form
# @para[in] : 2D matrix
# @para[out] : None
def spiralPrint(matrix):
    
    # number of rows
    m = len(matrix)
    
    # number of columns
    n = len(matrix[0])
    
    # starting index for the row
    k = 0
    
    # starting index for column
    l = 0
    
    while k<m and l <n:
        # print the first row #1,2,3,4
        for i in range(n):
            print(matrix[k][i])
        k = k + 1
        
        # print the last column   #8,12,16
        for i in range(k,m):
            print(matrix[i][n-1])
        n = n - 1
        
        # print the last row
        if k < m :
            for i in range(n-1,(l-1),-1):
                print(matrix[m-1][i])
            m = m - 1
        
        # print the first column in reversed
        if l < n:
            for i in range(m-1,k-1,-1):
                print(matrix[i][l])
            l = l + 1
            
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiralPrint(matrix)





