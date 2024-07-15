if __name__ == '__main__':
    n = int(input())
    dp = [0] * (n + 3)
    dp[1] = 0
    dp[2] = 1

    for i in range(3, n + 1):
        tmp = int(1e9)
        if i % 2 == 0:
            tmp = min(dp[i // 2] + 1, tmp)
        if i % 3 == 0:
            tmp = min(dp[i // 3] + 1, tmp)
        tmp = min(dp[i - 1] + 1, tmp)
        dp[i] = tmp
    print(dp[n])
