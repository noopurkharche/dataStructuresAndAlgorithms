class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True
        
    def findWord(self, ch, node):
        if not node:
            node = self.root
        if ch not in node.children:
            return (False, None)
        next_node = node.children[ch]
        return (True, next_node)
    
class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.addWord(word)
            
        self.result = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.dfs(board, trie, row, col, '', None)
        return list(self.result)
        
    def dfs(self, board, trie, row, col, path, node):
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
            return
        
        curr_ch = board[row][col]
        
        found, next_node = trie.findWord(curr_ch, node)
        
        if next_node and next_node.end:
            self.result.add(path+curr_ch)
            
        if found:
            tmp = board[row][col]
            board[row][col] = '#'
            self.dfs(board, trie, row+1, col, path+curr_ch, next_node)
            self.dfs(board, trie, row-1, col, path+curr_ch, next_node)
            self.dfs(board, trie, row, col+1, path+curr_ch, next_node)
            self.dfs(board, trie, row, col-1, path+curr_ch, next_node)
            board[row][col] = tmp
            
obj = Solution()
board = [['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']]
  
words = ["oath","pea","eat","rain"]

print(obj.findWords(board, words))
