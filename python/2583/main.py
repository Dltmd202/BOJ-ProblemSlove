from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
visit = [[0] * n for _ in range(m)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
square = []
count = 0
counts = []


def bfs(y, x, count):
    q = deque()
    visit[y][x] = True
    q.append((y, x))
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 0 and not visit[ny][nx]:
                visit[ny][nx] = count
                cnt += 1
                q.append((ny, nx))
    counts.append(cnt)


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visit[i][j]:
            count += 1
            bfs(i, j, count)

print(count)
print(' '.join(str(c) for c in sorted(counts)))