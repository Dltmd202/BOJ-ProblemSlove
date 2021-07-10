from collections import deque
import sys
input = sys.stdin.readline

tb = int(input())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for t in range(tb):
    m, n, k = map(int, input().split())
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    cnt = 0
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1


    def bfs(y, x):
        visited[y][x] = True
        q = deque()
        q.append((y, x))
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if graph[ny][nx] == 1 and not visited[ny][nx]:
                        q.append([ny, nx])
                        visited[ny][nx] = True
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)
