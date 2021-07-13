import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
q = deque()
res = []

for i in range(m):
    fr, bh = map(int, input().split())
    graph[fr].append(bh)
    ind[bh] += 1

for i in range(1, n + 1):
    if ind[i] == 0:
        q.append(i)
        res.append(i)

while q:
    now = q.popleft()
    for will in graph[now]:
        ind[will] -= 1
        if ind[will] == 0:
            q.append(will)
            res.append(will)

print(' '.join(str(r) for r in res))