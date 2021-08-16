import heapq
import sys
input = sys.stdin.readline

inf = sys.maxsize
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

dest = list(map(int, input().split()))
distance = [[inf] * (n + 1) for _ in range(3)]


def dijkstra(turn, start):
    q = []
    distance[turn][start] = 0
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)
        if distance[turn][now] < dist:
            continue
        for c, will in graph[now]:
            cost = c + dist
            if distance[turn][will] > cost:
                heapq.heappush(q, [cost, will])
                distance[turn][will] = cost


dijkstra(0, 1)
dijkstra(1, dest[0])
dijkstra(2, dest[1])
answer = (distance[0][dest[0]] + distance[1][dest[1]] + distance[2][n],
             distance[0][dest[1]] + distance[2][dest[0]] + distance[1][n])
print(min(answer) if min(answer) < inf else -1)
