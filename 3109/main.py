import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

c, r = map(int, input().split())
graph = [list(input()) for _ in range(c)]
visited = [[False] * (r + 1) for _ in range(c)]
goal = []
answer = 0
dy = [-1, 0, 1]
dx = [1, 1, 1]


def dfs(y, x):
    global answer
    if x == r - 1:
        answer += 1
        return True
    for i in range(3):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < c and 0 <= nx < r and graph[ny][nx] != 'x' and not visited[ny][nx]:
            visited[ny][nx] = True
            if dfs(ny, nx):
                return True


for i in range(c):
    visited[i][0] = True
    dfs(i, 0)

print(answer)
