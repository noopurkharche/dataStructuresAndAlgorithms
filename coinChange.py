# coin change [problem dynamic solution
def coinChange(coins, amount):
    dp = [0] + [amount + 1] * amount
    for i in range(1, amount + 1):
        for c in coins:
            if i >=  c:
                dp[i] = min(dp[i-c] + 1, dp[i])
    print(dp)
    if dp[amount] == amount+1:
            return -1
    return dp[amount]

coin = [1,2,5]
total = 11
print(coinChange(coin, total))
