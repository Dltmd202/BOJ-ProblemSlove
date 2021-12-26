from collections import deque
import sys
input = sys.stdin.readline
inf = int(1e9)

m, n = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]
visited = [[inf] * m for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
days = 0
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 0
        elif graph[i][j] == -1:
            visited[i][j] = -1

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 0 and visited[ny][nx] > visited[y][x] + 1:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

max_val = max(list(map(max, *visited)))
if max_val >= inf:
    print(-1)
else:
    print(max_val)
