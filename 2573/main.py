from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
buf = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dy = [0, -1, 1, 0]
dx = [1, 0, 0, -1]

year = 0
block = 0


def bfs(y, x, visited):

    q = deque([(y, x)])
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    for j in range(4):
                        if 0 <= ny + dy[j] < n and 0 <= nx + dx[j] < m:
                            buf[ny + dy[j]][nx + dx[j]] += 1
                    visited[ny][nx] = True
                if graph[ny][nx] != 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True


while True:
    block = 0
    visited = deepcopy(visit)

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i, j, visited)
                block += 1
    if block > 1:
        print(year)
        break
    elif block == 1:
        year += 1
        for i in range(n):
            for j in range(m):
                if graph[i][j]:
                    graph[i][j] = max(0, graph[i][j] - buf[i][j])
                    buf[i][j] = 0
    elif block == 0:
        print(0)
        break




