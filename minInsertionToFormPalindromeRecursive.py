def getMinInsertion(str1, left, right):
    
    # base case 1
    # if left and right pointers are out of bounds
    if left > right:
        return float("inf")
    
    # base case 2
    # if both pointers are pointing to same character 
    # or there is only on character then return 0
    if left == right:
        return 0
    
    # base case 3
    # if there are only two characters remaining
    # eg if ab is remaining then return 1
    # or if aa is remianing then return 0
    if left == right - 1:
        if str1[left] == str1[right]:
            return 0
        else:
            return 1
    
    if str1[left] == str1[right]:
        return getMinInsertion(str1, left + 1, right - 1)
    else:
        return min(getMinInsertion(str1, left + 1, right), getMinInsertion(str1, left, right - 1)) + 1



word = "abc"
left = 0
right = len(word) -1
print(getMinInsertion(word, left, right))
