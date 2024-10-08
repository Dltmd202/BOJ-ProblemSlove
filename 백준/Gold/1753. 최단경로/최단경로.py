import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

if __name__ == '__main__':
    V, E = map(int, input().split())
    K = int(input())
    distance = [INF] * (V + 1)
    graph = [[] for _ in range(V + 1)]


    def dijkstra(start):
        distance[start] = 0
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            pc, now = heapq.heappop(pq)

            if distance[now] < pc:
                continue

            for nc, next in graph[now]:
                next_cost = nc + pc

                if next_cost < distance[next]:
                    distance[next] = next_cost
                    heapq.heappush(pq, (next_cost, next))

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    dijkstra(K)

    for i in range(1, V + 1):
        print("INF" if distance[i] == INF else distance[i])
