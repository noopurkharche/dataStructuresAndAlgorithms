def prisonAfterNDays(cells, N):
    for i in range(0,N):
        #print(i+1)
        temp = []
        for i in range(0,len(cells)):
            temp.append(cells[i])
        for j in range(0,len(cells)):
            if j == 0 or j == len(cells)-1:
                if temp[j] == 1:
                    cells[j] = 0
            else:
                if temp[j-1] == temp[j+1]:
                    cells[j] = 1 
                else:
                    cells[j] = 0
        #print(cells)
        #print(temp)



cells = [0,1,0,1,1,0,0,1] 
#cells = [1,0,0,1,0,0,1,0]
# output [0,0,1,1,0,0,0,0]
N = 7
#N = 1000000000
N = N%14 
if not N:
    N = 14
print("0")
print(cells)
prisonAfterNDays(cells, N)

print(cells)

