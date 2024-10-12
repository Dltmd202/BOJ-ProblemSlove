if __name__ == '__main__':
    n, k = map(int, input().split())
    knapsack = []

    for i in range(n):
        a, b = map(int, input().split())
        knapsack.append((a, b))

    knapsack.sort(key=lambda x: x[0])
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(1, k + 1):
            if j >= knapsack[i][0]:
                dp[i][j] = max(dp[i - 1][j], knapsack[i][1] + dp[i - 1][j - knapsack[i][0]])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n - 1][k])

