# price query question
# frequency of maximum value 

price = [5,4,5,3,2]
query = [1,2,3,4]
# answer = [2,1,1,1,1]

#price = [2,2,2]
#query = [1,2,3]
# answer = [3,2,1]

#price = [2,1,2]
#query = [1,2,3]
# answer = [2,1,1]

maxArray = []
dict = {}

maxval = -float("inf")
print(maxval)

for i in range(len(price)-1,-1,-1):
    
    # construct dictionary of items and price as key and value as number of occurences
    if price[i] not in dict:
        dict[price[i]] = 1 
    else:
        dict[price[i]] = dict[price[i]] + 1
        
    # get the maximum value at every index
    if maxval < price[i]:
        maxval = price[i]
        maxArray.append(maxval)
    else:
        maxArray.append(maxval)
maxArray = maxArray[::-1]

print(maxArray)

result = []

# for every item in query
for index in query:
    
    # check if it is the same as in price and maxArray
    # if so decrement the counter and append in result 
    # else just append in result 
    if price[index-1] == maxArray[index-1]:
        result.append(dict[price[index-1]])
        dict[price[index-1]] = dict[price[index-1]] - 1
    else:
        result.append(dict[price[index-1]])

print(result)
        
    
