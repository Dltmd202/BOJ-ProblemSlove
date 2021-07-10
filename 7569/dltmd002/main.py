from collections import deque
import sys
input = sys.stdin.readline
inf = int(1e10)

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[inf] * m for _ in range(n)] for _ in range(h)]
dz = [0, 0, 0, 0, -1, 1]
dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k])
                visited[i][j][k] = 0
            elif graph[i][j][k] == -1:
                visited[i][j][k] = -1

while q:
    z, y, x = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if graph[nz][ny][nx] == 0 and visited[nz][ny][nx] > visited[z][y][x] + 1:
                q.append([nz, ny, nx])
                visited[nz][ny][nx] = visited[z][y][x] + 1


max_val = 0
for i in range(h):
    for j in range(n):
        max_val = max(max_val, max(visited[i][j]))

print(-1 if max_val >= inf else max_val)
