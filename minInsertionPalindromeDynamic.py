word = "geeks"

dp = []

for i in range(len(word)):
    col = []
    for j in range(len(word)):
        col.append(0)
    dp.append(col)
    
for leng in range(1, len(word)):
    h = leng
    for l in range(len(word)):
        if h >= len(word):
            break
        if word[l] == word[h]:
            dp[l][h] = dp[l + 1][h - 1]
        else:
            dp[l][h] = min(dp[l+1][h], dp[l][h-1]) + 1
        h = h + 1
print(dp)
print(dp[0][len(word)-1])
