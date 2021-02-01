import heapq
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegrees = [0] * (n + 1)
turn = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegrees[b] += 1

q = deque()

for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append((i, i))

while q:
    now, turn = q.popleft()
    print(now, end=' ')
    for will in graph[now]:
        indegrees[will] -= 1
        if indegrees[will] == 0:
            q.append((will, turn + 1))

