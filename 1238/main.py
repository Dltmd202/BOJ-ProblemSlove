import heapq
import sys
input = sys.stdin.readline
MAX = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
go = [MAX] * (n + 1)
back = [MAX] * (n + 1)
answer = 0
for i in range(m):
    now, will, cost = map(int, input().split())
    graph[now].append((cost, will))


def dijkstra(x):
    distance = [MAX] * (n + 1)
    q = []
    distance[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for c, will in graph[now]:
            cost = c + dist
            if distance[will] > cost:
                distance[will] = cost
                heapq.heappush(q, (cost, will))
    return distance


for i in range(1, n + 1):
    go[i] = dijkstra(i)[x]
back = dijkstra(x)

for g, b in zip(go[1:], back[1:]):
    answer = max(answer, g + b)

print(answer)