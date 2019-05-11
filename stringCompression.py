
# method to compress the string in the given format
# @para[in] : takes input as string
# @para[out]: returns the compressed string
def compressString(s):
    r = ""
    l = len(s)
    
    # Check for edge cases
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    
    count = 1
    i = 1
    
    while i < l:
		# check if current character is same as the previous character and increment count
		# if current aand previous character are not same than append count with the character
        if s[i] == s[i-1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1
        i += 1
	# check for one last condition after the loop
    r = r + s[i -1] + str(count)
	
    return r

	
s = 'aaabbbccc'
compressedString = compressString(s)
print(compressedString)