from collections import deque
import sys

input = sys.stdin.readline
INF = -sys.maxsize
DOWN = 0
RIGHT = 1
LEFT = 2

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]
dy = [1, 0, 0]
dx = [0, 1, -1]
q = deque()
q.append((0, 0, 0))
dp[0][0][0] = graph[0][0]
dp[0][0][1] = graph[0][0]
dp[0][0][2] = graph[0][0]
for j in range(1, m):
    dp[0][j][RIGHT] = graph[0][j] + dp[0][j - 1][RIGHT]
# print(dp)
for i in range(1, n):
    dp[i][0][DOWN] = dp[i][0][RIGHT] = max(dp[i - 1][0]) + graph[i][0]
    dp[i][m - 1][DOWN] = dp[i][m - 1][LEFT] = max(dp[i - 1][m - 1]) + graph[i][m - 1]
    for j in range(1, m):
        dp[i][j][DOWN] = max(dp[i - 1][j]) + graph[i][j]
    for j in range(1, m):
        dp[i][j][RIGHT] = max(dp[i][j - 1][RIGHT], dp[i][j - 1][DOWN]) + graph[i][j]
    for j in range(m - 2, -1, -1):
        dp[i][j][LEFT] = max(dp[i][j + 1][LEFT], dp[i][j + 1][DOWN]) + graph[i][j]
# print('\n'.join(str(d) for d in dp))
print(max(dp[n - 1][m - 1]))