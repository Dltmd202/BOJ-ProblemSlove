from collections import deque
import sys
input = sys.stdin.readline
import heapq
inf = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distance = [inf] * (v + 1)
q = []
heapq.heappush(q, [0, k])
distance[k] = 0

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])


while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for c, will in graph[now]:
        cost = dist + c
        if cost < distance[will]:
            distance[will] = cost
            heapq.heappush(q, [cost, will])

for res in distance[1:]:
    if res >= inf:
        print('INF')
    else:
        print(res)