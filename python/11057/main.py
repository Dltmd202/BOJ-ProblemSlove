MAX = 10007
n = int(input())

dp = [[1] * 10 for _ in range(n + 2)]

for i in range(2, n + 1):
    dp[i][0] = sum(dp[i - 1])
    for j in range(1, 10):
        dp[i][j] = (dp[i][j - 1] - dp[i -1][j - 1]) % MAX

print(sum(dp[n]) % MAX)