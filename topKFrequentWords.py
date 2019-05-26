# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. 
# If two words have the same frequency, then the word with the lower alphabetical order comes first.


def topKFrequent(words, k):
    bucket= [[] for _ in range(len(words)+1)]
    dic={}
    
    for word in words:
        dic[word]= dic.get(word, 0)+1
    
    for word in dic:
        bucket[dic[word]].append(word)
        
    res=[]
    
    for i in range(len(bucket)-1, -1, -1):
        if not bucket[i]:
            continue
        bucket[i].sort()
        if len(bucket)< k-len(res):
            res+= bucket[i]
        else:
            res+= bucket[i][:k-len(res)]
    
    return res 
    
    
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(words, k))
