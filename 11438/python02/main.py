import sys
from math import log2
from collections import deque

n = int(sys.stdin.readline())
log = int(log2(n) + 1)
graph =[[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[0] * log for _ in range(n + 1)]
depth = [0] * (n + 1)
visit = [False] * (n + 1)

q = deque()
q.append(1)
visit[1] = True
while q:
    now = q.popleft()
    for will in graph[now]:
        if not visit[will]:
            visit[will] = True
            q.append(will)
            parent[will][0] = now
            depth[will] = depth[now] + 1

for i in range(1, log):
    for j in range(1, n + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

m = int(sys.stdin.readline())
answer = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(log - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        answer.append(a)
        continue

    for i in range(log - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    answer.append(parent[a][0])

print('\n'.join(str(num) for num in answer))