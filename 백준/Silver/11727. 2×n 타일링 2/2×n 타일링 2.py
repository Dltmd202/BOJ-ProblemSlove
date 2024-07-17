if __name__ == '__main__':
    MOD = 10_007
    n = int(input())

    dp = [[0] * 4 for _ in range(n + 4)]
    dp[1][0] = 1
    dp[1][1] = 1

    dp[2][0] = 3
    dp[2][1] = 1
    dp[2][2] = 1
    dp[2][3] = 1

    for i in range(3, n + 1):
        dp[i][1] = dp[i - 1][0]
        dp[i][2] = dp[i - 2][0]
        dp[i][3] = dp[i - 2][0]
        dp[i][0] = sum(dp[i][1:])

    print(dp[n][0] % MOD)
