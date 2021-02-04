from collections import deque
import sys
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[0] * (m + 1)]
    visit = [[0] * (m + 1) for _ in range(n + 1)]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        graph.append([0] + data)


    def bfs(y, x, cnt):
        q = deque()
        q.append((i, j, cnt))
        while q:
            y, x, count = q.popleft()
            for k in range(8):
                ny = y + dy[k]
                nx = x + dx[k]
                if 1 <= nx <= m and 1 <= ny <= n:
                    if graph[ny][nx] == 1 and visit[ny][nx] == 0:
                        visit[ny][nx] = cnt
                        q.append((ny, nx, cnt))


    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] == 1 and visit[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)

    print(cnt)
