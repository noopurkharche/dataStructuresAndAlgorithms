# method to traverse the borad in dfs fashion vertically or horzontally about a given ccharacter
# para[in] : word : word to Search
# para[in] : borad : given board
# para[in] : x,y : current point on the board
# para[in] : index : current index of the word
# para[out] : True or False
def dfs(word, board, x, y, index):
    
    if index == len(word):
        return True
    
    if x<0 or x>=len(board) or y<0 or y>=len(board[0]) or word[index] != board[x][y] or board[x][y] == "*":
        return False
    
    board[x][y] = "*"
    finalAns = dfs(word,board, x-1,y,index + 1) or dfs(word,board, x+1,y,index +1) or dfs(word,board, x,y-1,index+1) or dfs(word,board, x,y+1,index+1)
    board[x][y] = word[index]
    return finalAns

# this method prints true if a given word is present in the board 
# when search in horzonatal and vertical fashion about given index
# para[in] : word : word to Search
# para[in] : board : given board
# para[out] : None
def wordSearch(word,board):
    for i in range(len(board)):
        for j in range(len(board[0])):
           if dfs(word, board,i,j,0):
                print('True')
                return
    print('False')
    return

# initialize the board
board =[['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]

# test case 1
word = "ABCCED"
wordSearch(word,board)

#test case 2
word = "SEE"
wordSearch(word,board)

# test case 3
word = "ABCB"
wordSearch(word,board)