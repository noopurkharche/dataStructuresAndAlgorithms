=# method for longestPalindrome substring
# considers each character as cenyter and find the longest palindrome around it
# @para[in] : s - inputString
# @para[out]: None
def longestPalindrome(s):
        max_length = 1
        
        # initialize the start
        start = 0
        # end of the string to length
        end = len(s)
        
        l = 0
        h = 0
        
        for i in range(1, len(s)):
            
            # Checking for even length palindrome
            l = i-1
            h = i
            while l >=0 and h<len(s) and s[l] == s[h]:
                if h-l+1 > max_length:
                    start = l
                    max_length = h-l+1
		#expand around
                l -= 1
                h += 1
            
            # Checking for odd length palindromes
            l = i - 1
            h = i + 1
            while l>=0 and h<len(s) and s[l] == s[h]:
                if h-l+1 > max_length:
                    start = l
                    max_length = h-l+1
		#expand around the center character
                l -= 1
                h += 1
        #printing the longest length palidrome
        print(s[start:start+max_length])
        
longestPalindrome('abaxabaxabb')        
