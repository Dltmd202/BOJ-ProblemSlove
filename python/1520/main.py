import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
c, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(c)]
visited = [[-1] * r for _ in range(c)]
answer = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(y, x):
    if y == c - 1 and x == r - 1:
        return 1
    if visited[y][x] == -1:
        visited[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < c and 0 <= nx < r and graph[y][x] > graph[ny][nx]:
                visited[y][x] += dfs(ny, nx)
    return visited[y][x]


print(dfs(0, 0))

