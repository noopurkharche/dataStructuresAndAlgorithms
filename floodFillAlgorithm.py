# flood fill algorithm

def dfs(screen,preVal,newVal,x,y):
    
    # bounding conditions
    if x < 0 or x >= len(screen) or y < 0 or y >= len(screen[0]) or screen[x][y] != preVal:
        return
    
    # make it visited or fill
    screen[x][y] = newVal
    
    # go in depth first fashion
    dfs(screen,preVal,newVal,x+1,y)
    dfs(screen,preVal,newVal,x-1,y)
    dfs(screen,preVal,newVal,x,y+1)
    dfs(screen,preVal,newVal,x,y-1)







screen = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 1, 1],
                [1, 2, 2, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 2, 2, 0],
                [1, 1, 1, 1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1, 2, 2, 1]]
                
print("-----------Before Fill-----------")
for i in range(len(screen)):
    print(screen[i])
    
preVal = screen[4][4]
dfs(screen,preVal,3,4,4)

print("-----------After Fill-----------")
for i in range(len(screen)):
    print(screen[i])

                
