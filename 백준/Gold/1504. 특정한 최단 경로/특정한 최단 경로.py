import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)


if __name__ == '__main__':
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for i in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    v1, v2 = map(int, input().split())

    def dijkstra(start):
        distance = [INF] * (N + 1)
        distance[start] = 0
        pq = [(0, start)]

        while pq:
            dist, now = heapq.heappop(pq)

            if distance[now] < dist:
                continue

            for cost, will in graph[now]:
                if cost + dist < distance[will]:
                    heapq.heappush(pq, (cost + dist, will))
                    distance[will] = cost + dist

        return distance

    start_dist = dijkstra(1)
    v1_dist = dijkstra(v1)
    v2_dist = dijkstra(v2)

    ans1 = start_dist[v1] + v1_dist[v2] + v2_dist[N]
    ans2 = start_dist[v2] + v2_dist[v1] + v1_dist[N]
    min_val = min(ans1, ans2)

    print(min_val if min_val < INF else -1)
