import sys
input = sys.stdin.readline
t = int(input())

for tb in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    res = 0

    def get_score():
        global res
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        res = max(dp[0][0], dp[1][0])
        if n == 1:
            return res
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]
        res = max(res, dp[0][1], dp[1][1])
        if n == 2:
            return max(dp[0][1], dp[1][1])
        else:
            for i in range(2, n):
                dp[0][i] = sticker[0][i] + max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2])
                dp[1][i] = sticker[1][i] + max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2])
                res = max(res, dp[0][i], dp[1][i])

    get_score()
    print(res)
