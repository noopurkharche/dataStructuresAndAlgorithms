#subarray with given sum
arr = [1,7,4,3,1,2,1,5,1]
target = 7

currentSum = arr[0]
start = 0
i = 1
n = len(arr)

while i <= n:
    while currentSum > target and start < i-1:
        currentSum = currentSum - arr[start]
        start = start + 1
        
    if currentSum == target:
        print(start)
    
    if i < n:
        currentSum = currentSum + arr[i]
    i = i + 1
