from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
dy = [0, -1, 0, 1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
answer = 0
q = deque()


def bfs():
    global answer
    while q:
        z, y, x = q.popleft()
        answer = max(answer, visited[z][y][x])
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if graph[nz][ny][nx] == 0 and visited[nz][ny][nx] == -1:
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nz, ny, nx))


for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1 and visited[k][i][j] == -1:
                q.append((k, i, j))
                visited[k][i][j] = 1
            if graph[k][i][j] == -1:
                visited[k][i][j] = 0
bfs()
res = True
for k in range(h):
    for i in range(n):
        for j in range(m):
            if visited[k][i][j] == -1:
                res = False
                break
if res:
    print(answer - 1)
else:
    print(-1)