from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[-1] * m for _ in range(n)]
graph = [list(map(lambda x: x - ord('0'), map(ord, input().rstrip()))) for _ in range(n)]
parent = [i for i in range(n * m)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
q = deque()
counters = dict()
ids = []


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def get_id(y, x):
    return y * m + x


def bfs(y, x):
    id = get_id(y, x)
    ids.append(id)
    counters[id] = 1
    q = deque()
    q.append([y, x])
    visited[y][x] = id
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == -1 and graph[ny][nx] == 0:
                    visited[ny][nx] = id
                    counters[id] += 1
                    q.append([ny, nx])
                    nid = get_id(ny, nx)
                    union(id, nid)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            id_list = set()
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0 <= ni < n and 0 <= nj < m:
                    nid = find(get_id(ni, nj))
                    if graph[ni][nj] == 0 and nid not in id_list:
                        graph[i][j] += counters[find(get_id(ni, nj))]
                        id_list.add(nid)

print('\n'.join(''.join(str(c % 10) for c in r) for r in graph))