import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())
q = []
heapq.heappush(q, (0, start, [start]))
dist[start] = 0


def dijkstra(start):
    answer = []
    while q:
        c, now, way = heapq.heappop(q)
        if dist[now] < c:
            continue
        for d, will in graph[now]:
            cost = d + c
            if dist[will] > cost:
                dist[will] = cost
                if will == end and dist[end] > c:
                    answer = way[:] +[will]
                heapq.heappush(q, (cost, will, way + [will]))
    return answer

answer = dijkstra(start)
print(dist[end])
print(len((answer)))
print(' '.join(str(i) for i in answer))