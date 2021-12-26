from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
visit = [[False] * m for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def change(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

q = deque()
q.append((r, c, d))
visit[r][c] = True
cnt = 0
if graph[r][c] == 0:
    cnt = 1
direction = d

while q:
    y, x, d = q.popleft()
    direction = d
    for rotation in range(4):
        direction = change(direction)
        ny = y + dy[direction]
        nx = x + dx[direction]

        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0 and not visit[ny][nx]:
            visit[ny][nx] = 1
            q.append((ny, nx, direction))
            cnt += 1
            break
        elif rotation == 3:
            ny = y + dy[back(direction)]
            nx = x + dx[back(direction)]
            if graph[ny][nx] == 0:
                q.append((ny, nx, d))

print(cnt)
