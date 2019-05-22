arr = [-1,0,1,2,-1,-4]
arr.sort()
print(arr)
sum = 0
for i in range(0,len(arr)-3):
    if i == 0 or arr[i]> arr[i-1]:
        start = i + 1
        end = len(arr) - 1
    
        while start < end:
            if (arr[i] + arr[start] + arr[end]) == sum:
                print(str(arr[i]) + " " + str(arr[start]) + " " + str(arr[end]))
            if (arr[i] + arr[start] + arr[end]) < sum:
                currentStart = start
                while arr[currentStart] == arr[start] and start < end:
                    start = start + 1
            else:
                currentEnd = end
                while arr[currentEnd] == arr[end] and start < end:
                    end = end - 1
                
