def ladderLength(beginWord, endWord, wordList):
    queue = [(beginWord, 1)]
    visited = set()
    
    while queue:
        word, dist = queue.pop(0)
        if word == endWord:
            return dist
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                tmp = word[:i] + j + word[i+1:]
                print("made word - " + tmp)
                if tmp not in visited and tmp in wordList:
                    print("in Queue - " + tmp)
                    queue.append((tmp, dist+1))
                    visited.add(tmp)
    return 0
    
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
ladderLength(beginWord, endWord, wordList)
