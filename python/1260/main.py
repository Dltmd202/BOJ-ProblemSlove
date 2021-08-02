from collections import deque
from copy import deepcopy

v, e, start = map(int, input().split())
graph = [[]for i in range(v + 1)]
d = []
b = []
visited = [False for i in range(v + 1)]
for i in range(e):
    now, will = map(int, input().split())
    graph[now].append(will)
    graph[will].append(now)


def dfs(start, visited):
    visited[start] = True
    d.append(start)
    for will in graph[start]:
        if not visited[will]:
            dfs(will, visited)


def bfs(start, visited):
    visited[start] = True
    q = deque()
    q.append(start)
    b.append(start)
    while q:
        now = q.popleft()
        for will in graph[now]:
            if not visited[will]:
                b.append(will)
                visited[will] = True
                q.append(will)


for i in range(1, v + 1):
    graph[i].sort()

visit = deepcopy(visited)
dfs(start, visit)
visit = deepcopy(visited)
bfs(start, visit)
print(' '.join(str(v) for v in d))
print(' '.join(str(v) for v in b))
