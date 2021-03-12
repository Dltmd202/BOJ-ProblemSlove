import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]
answer = int(1e9)
data = [[0, 0, 0]] + data

for first in range(3):
    for i in range(3):
        if first == i:
            dp[1][i] = data[1][i]
        else:
            dp[1][i] = INF
    for i in range(2, n + 1):
        dp[i][0] = data[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = data[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = data[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    for i in range(3):
        if i == first:
            continue
        answer = min(answer, dp[n][i])

print(answer)