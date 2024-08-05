if __name__ == '__main__':
    n = int(input())
    data = [int(input()) for _ in range(n)]

    def solution():
        if n == 1:
            return data[0]
        elif n == 2:
            return data[0] + data[1]

        dp = [0] * (n + 2)
        dp[0] = data[0]
        dp[1] = data[0] + data[1]
        dp[2] = max(data[2] + data[0], data[2] + data[1], dp[1])
        for i in range(3, n):
            dp[i] = max(data[i] + dp[i - 2], data[i] + data[i - 1] + dp[i - 3], dp[i - 1])
        return max(dp)

    print(solution())
