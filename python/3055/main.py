from collections import deque

c, r = map(int, input().split())
graph = [list(input()) for _ in range(c)]
visit = [[-1] * r for _ in range(c)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

q = deque()
water = []
s = []
for i in range(c):
    for j in range(r):
        if graph[i][j] == '*':
            water.append((i, j))
            visit[i][j] = 0
        elif graph[i][j] == 'S':
            s.append((i, j))
            visit[i][j] = 0

for w in water:
    q.append(w)
q.append(*s)


def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < c and 0 <= nx < r and not graph[ny][nx] == 'X':
                if graph[ny][nx] == 'D' and graph[y][x] == 'S':
                    return True, str(visit[y][x] + 1)
                if graph[ny][nx] == 'D' and graph[y][x] == '*':
                    continue
                if graph[ny][nx] == '.' and visit[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x]
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny, nx))
    return False, "KAKTUS"


print(bfs()[1])
