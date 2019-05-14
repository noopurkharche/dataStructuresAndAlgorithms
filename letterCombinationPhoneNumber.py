# main mehtod
# @para[in] : digits -string input which is comnbination of digits
# @para[out] : None
def letterCombinations(digits):
    answer = []
    if digits == "":
        return answer
    matcher = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
    dfs(digits,answer, 0, "", matcher)
    print(answer)
    
# method to traverse in depth first fashion
# @para[in]: digits, output - ouput list will contain the final combinations of letterCombinations
# @para[in]: index - thee current index, current- the current combination of letters
# @para[in]: the predefined combination of numbers to leteers iin phone key pad
# @para[out]: None
def dfs(digits,output, index, current, matcher):
    
    if index == len(digits):
        output.append(current)
        return
    str1 = matcher[int(digits[index])]
    for i in range(len(str1)):
        dfs(digits, output, index+1, current + str1[i],matcher)


letterCombinations('23')
        
