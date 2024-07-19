if __name__ == '__main__':
    n = int(input())

    dp = [[0] * 2 for _ in range(n + 4)]
    dp[1][1] = 1
    dp[2][0] = 1
    dp[3][0] = 1
    dp[3][1] = 1

    for i in range(4, n + 1):
        dp[i][0] = sum(dp[i - 1])
        dp[i][1] = dp[i - 1][0]

    print(sum(dp[n]))
