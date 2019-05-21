    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """   
        checkStringSet = set()
        left = 0 
        right = 0
        charset = set()
        max_len = 0
	
        while right < len(s):
            if s[right] in charset:
                charset.remove(s[left])
                left = left +  1
            else:
                charset.add(s[right])
                right = right + 1
                if len(charset) > max_len:
                    max_len = len(charset)
        return max_len
