tb = int(input())
dp = [[0, 0] for _ in range(50)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 50):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for t in range(tb):
    n = int(input())
    zeros = 0
    ones = 0
    print(dp[n][0], dp[n][1])
