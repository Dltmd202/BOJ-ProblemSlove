import  heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n , m = map(int,input().split())


graph = [[] for _ in range(n+1)]


for i in range(m):
    a , b , c = map(int,input().split())
    graph[a].append((c,b))

    graph[b].append((c,a))

v = list(map(int,input().split()))

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q , (0 ,start))

    while q:
        dist , now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for co , will in graph[now]:
            cost = dist + co
            if cost < distance[will]:
                heapq.heappush(q,(cost , will))
                distance[will] = cost
    return distance

dist1 = dijkstra(1)
distv0 = dijkstra(v[0])
distv1 = dijkstra(v[1])
answer = min(dist1[v[0]] + distv1[n] , dist1[v[1]] + distv0[n]) + distv0[v[1]]
if answer >= INF:
    print(-1)
else:
    print(answer)