if __name__ == '__main__':
    n = int(input())
    data = list(int(input()) for _ in range(n))

    def solution():
        if n == 1:
            return data[0]

        dp = [[0] * 2 for _ in range(n + 3)]
        dp[0][0] = data[0]
        dp[0][1] = data[0]
        dp[1][0] = dp[0][0] + data[1]
        dp[1][1] = data[1]

        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][1], dp[i - 2][0]) + data[i]
            dp[i][1] = max(dp[i - 2]) + data[i]

        return max(dp[n - 1])
    print(solution())
