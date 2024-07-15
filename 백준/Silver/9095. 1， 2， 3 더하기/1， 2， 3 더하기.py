if __name__ == '__main__':
    n = int(input())
    data = list(int(input()) for _ in range(n))
    max_val = max(data)
    dp = [0] * (max_val + 3)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, max_val + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for d in data:
        print(dp[d])