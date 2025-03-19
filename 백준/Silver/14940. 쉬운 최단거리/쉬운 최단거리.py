from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    sy, sx = 0, 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                sy, sx = i, j
            if graph[i][j] == 0:
                dist[i][j] = 0

    q = deque([(sy, sx)])
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                if dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

    for d in dist:
        print(' '.join(map(str, d)))
