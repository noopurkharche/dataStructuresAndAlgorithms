arr = [2,3,1,1,4]

# check edge comndition if one element present in the array
if  len(nums) ==1 :
    print(0)
    
# array length is zero or array is empty
if len(nums) == 0:
    print(-1)

maxReach = arr[0]
step = arr[0]
jump = 1
flag = 0


for i in range(1,len(arr)):
    if i == len(arr) -1:
        print("----" + str(jump))
        flag = 1
        break
        
    naxReach = max(maxReach, i + arr[i])
    step = step - 1
    if step == 0:
        jump = jump + 1 
        step = maxReach - i
if flag == 0:
    print(str(-1))
    
