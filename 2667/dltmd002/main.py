from collections import deque, defaultdict

n = int(input())
graph = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
cnt = 0
counter = defaultdict(int)


def bfs(y, x):
    global cnt
    cnt += 1
    visited[y][x] = cnt
    counter[cnt] += 1
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == '1' and visited[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = cnt
                    counter[cnt] += 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and visited[i][j] == 0:
            bfs(i, j)

count = []
for i in counter:
    count.append(counter[i])
print(len(count))
print('\n'.join(str(c) for c in sorted(count)))
