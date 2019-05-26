# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
#
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another
# character in this word, the modified word is in the dictionary you just built.


class TrieNode(object):
    def __init__(self):
        self.isAend = False
        self.contains = {}


class MagicDictionary(object):
  
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        
        r = self.root
        
        for chr in word:
            if chr not in r.contains:
                r.contains[chr] = TrieNode()
            r = r.contains[chr]
        
        r.isAend = True
    
    def buildDict(self, dict):
        for word in dict:
            self.addWord(word)  
            
    def findWord(self, remain, r, word):
        if not word:
            return True if remain == 0 and r.isAend else False
        for key in r.contains.keys():
            if key == word[0]:
                if self.findWord(remain, r.contains[key], word[1:]):
                    return True
            elif remain == 1:
                if self.findWord(0, r.contains[key], word[1:]):
                    return True
        return False

    def search(self, word):
        return self.findWord(1, self.root, word)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
