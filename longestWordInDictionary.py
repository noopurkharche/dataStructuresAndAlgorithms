# Given a list of strings words representing an English Dictionary, find the longest word in words that can be 
# built one character at a time by other words in words. If there is more than one possible answer, return the longest word 
# with the smallest lexicographical order.
# If there is no answer, return the empty string.


# structure of trie node
class TrieNode:
    def __init__(self, word='', end=False):
        self.end = end
        self.word = word
        self.children = {}


# This function creates a trie data structure for all thee words in the words List
# and also finds the longest word in the dictionary 
# para[in] : words list as input
# para[out]: returns the longest word in the dictionary
def longestWord(words):
    # build Trie
    root = TrieNode()
    for word in words:
        #print("Current Word : " + word)
        cur = root
        for i, ch in enumerate(word):
            #print("Create Nodes for : ")
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                #print("Node : " + ch)
                nextNode = TrieNode()
                cur.children[ch] = nextNode
                cur = nextNode
            if i == len(word) - 1:
                #print("End of this word")
                cur.end = True
                cur.word = word
        
    # check Trie
    print(root.children.values())
    stack = list(root.children.values())
    # print(stack)
    res = ''
    print("-------------------------------------------")
    while stack:
        node = stack.pop(-1)
        if node.end:
            #print("Current" + node.word)
            # if the words are of the same length then take the word in lexicographical order
            if len(res) < len(node.word) or (len(res) == len(node.word) and res > node.word):
                #print("longest " + node.word)
                res = node.word
            stack.extend(list(node.children.values()))
    return res
        
words = ["w","wo","wor","worl", "world"]
print(longestWord(words))
