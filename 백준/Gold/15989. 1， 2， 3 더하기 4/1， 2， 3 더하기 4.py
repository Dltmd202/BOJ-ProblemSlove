if __name__ == '__main__':
    n = int(input())
    data = list(int(input()) for _ in range(n))
    dp = [[0] * 4 for _ in range(4 + max(data))]

    dp[1][1] = 1

    dp[2][1] = 1
    dp[2][2] = 1
    dp[2][3] = 0

    dp[3][1] = 2
    dp[3][2] = 0
    dp[3][3] = 1

    dp[4][1] = 3
    dp[4][2] = 1
    dp[4][3] = 0

    for i in range(5, max(data) + 1):
        dp[i][1] = sum(dp[i - 1])
        dp[i][2] = sum(dp[i - 2][2:])
        dp[i][3] = dp[i - 3][3]

    for d in data:
        print(sum(dp[d]))
