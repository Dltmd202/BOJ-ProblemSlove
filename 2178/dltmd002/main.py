from collections import deque
import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
graph = [input() for i in range(n)]
visited = [[inf] * m for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
q = deque()
q.append([0, 0])
visited[0][0] = 1

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == '1' and visited[ny][nx] > visited[y][x] + 1:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

print(visited[n - 1][m - 1])