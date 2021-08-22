from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
dp = [[1] * n for _ in range(n)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
answer = 0


def dfs(y, x):
    if dp[y][x] != 1:
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] > graph[y][x]:
                if dp[ny][nx] != 1:
                    dp[y][x] = max(dp[y][x], dp[ny][nx] + 1)
                else:
                    dp[y][x] = max(dp[y][x], dfs(ny, nx))
    return dp[y][x]


for i in range(n):
    for j in range(n):
        dfs(i, j)
print(dp)
print(answer)
