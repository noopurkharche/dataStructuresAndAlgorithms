# Subset Sum Problem Dynamic Programing

def subsetSum(input, total):
    
    dp = []
    # initialize the array to False
    for i in range(len(input) +1):
        temp = []
        for j in range(total + 1):
            temp.append(False)
        dp.append(temp)
        
    # make the first column to True as 0 can be formed 
    for i in range(len(input)):
        dp[i][0] = True
        
    for i in range(1,len(input) + 1):
        for j in range(1,total + 1):
            if j >= input[i-1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - input[i - 1]]
            else:
                dp[i][j] = dp[i-1][j]
                
    print(dp[len(input)][total])
                

input = [2,3,7,8]
total = 11
subsetSum(input, total)


