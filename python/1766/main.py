
from collections import deque
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegrees = [0] * (n + 1)
count = [0] * (n + 1)
rule = set()

for i in range(m):
    now, will = map(int, input().split())
    rule.add((now, will))
    indegrees[will] += 1
    graph[now].append(will)

q = []

for i in range(1, n + 1):
    if indegrees[i] == 0:
        heapq.heappush(q, i)

answer = []

while q:
    now = heapq.heappop(q)
    answer.append(now)
    for will in graph[now]:
        indegrees[will] -= 1
        if indegrees[will] == 0:
            heapq.heappush(q,will)


print(' '.join(str(node) for node in answer))