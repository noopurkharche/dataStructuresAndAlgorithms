def convert(s, numRows):
    posMap = {}
    flag = 1
    pos = 0
    
    for char in s:
        
        if pos == numRows:
            flag = 0
            
        if pos == 1:
            flag = 1
        
        # if flag is 1 then increment the position else decrement the position
        if flag == 1:
            pos = pos + 1
        else:
            pos = pos - 1
            
        if pos not in posMap:
            posMap[pos] = [char]
        else:
            posMap[pos].append(char)
            
    result = ""
    for key in posMap:
        result = result + "".join(posMap[key])
    print(result)            
    
# s = "PAYPALISHIRING"
# numRows = 3
# output PAHNAPLSIIGYIR

s = "PAYPALISHIRING"
numRows = 4
# output PINALSIGYAHRPI
convert(s, numRows)
