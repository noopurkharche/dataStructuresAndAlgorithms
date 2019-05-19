S = "ababcbacadefegdehijhklij"
j = 0
start = 0
lastOccurence = {}
for idx, val in enumerate(S):
    lastOccurence[val] = idx
    
result = []
for idx,val in enumerate(S):
    j = max(j, lastOccurence[val])
    if idx == j:
        result.append(idx - start + 1)
        start = idx + 1
print(result)
