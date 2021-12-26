from collections import deque
INF = int(1e9)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


c, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(c)]
visit = [[False] * r for _ in range(c)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

cnt = 0
q = deque()
for i in range(c):
    for j in range(r):
        if graph[i][j] == 1 and not visit[i][j]:
            cnt += 1
            q.append((i, j))
            graph[i][j] = cnt
            visit[i][j] = True
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < c and 0 <= nx < r and graph[ny][nx] == 1 and not visit[ny][nx]:
                        graph[ny][nx] = graph[y][x]
                        visit[ny][nx] = True
                        q.append((ny, nx))

degree = [[INF] * (cnt + 1) for _ in range(cnt + 1)]
visit = [[False] * r for _ in range(c)]
stack = deque()
for i in range(c):
    for j in range(r):
        if graph[i][j] != 0 and not visit[i][j]:
            for k in range(4):
                stack.append((i, j, 0))
                while stack:
                    y, x, cost = stack.pop()
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < c and 0 <= nx < r:
                        if graph[ny][nx] == 0:
                            stack.append((ny, nx, cost + 1))
                        elif cost > 1 and graph[i][j] != graph[ny][nx]:
                            degree[graph[i][j]][graph[ny][nx]] = min(
                                degree[graph[i][j]][graph[ny][nx]],
                                cost
                            )

edges = []
for i in range(1, cnt + 1):
    for j in range(1, cnt + 1):
        if degree[i][j] < INF:
            edges.append((degree[i][j], i, j))

edges.sort()
parents = [i for i in range(cnt + 1)]
answer = 0

for edge in edges:
    cost, now, will = edge
    if find_parent(parents, now) != find_parent(parents, will):
        union_parent(parents, now, will)
        answer += cost

result = True
for i in range(1, cnt + 1):
    if find_parent(parents, i) != 1:
        result = False

if result:
    print(answer)
else:
    print(-1)