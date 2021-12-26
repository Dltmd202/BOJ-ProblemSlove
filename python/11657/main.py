import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            will = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[will] > dist[cur] + cost:
                dist[will] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False


if bf(1):
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] >= INF:
            print(-1)
        else:
            print(dist[i])

