


import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

q = []
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for c, will in graph[now]:
        cost = dist + c
        if distance[will] > cost:
            heapq.heappush(q, (cost, will))
            distance[will] = cost

print(distance[end])





