# maximum sum subarray of size k [Time:O(n), Space:O(1)]
arr = [-1,2,3,1,-3,2]
k = 2

res = 0

# calculate the sum of the window of size k
for i in range(k):
    res = res + arr[i]
    
currSum = res
for i in range(k, len(arr)):
    # calculate the sum of the current window
    currSum = currSum + arr[i] - arr[i-k]
    res = max(res, currSum)

print(res)
