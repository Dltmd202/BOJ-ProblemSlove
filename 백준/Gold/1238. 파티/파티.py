import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

if __name__ == '__main__':
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    def dijkstra(start):
        pq = [(0, start)]
        distance = [INF] * (N + 1)
        distance[start] = 0

        while pq:
            dist, now = heapq.heappop(pq)

            if distance[now] < dist:
                continue

            for cost, next in graph[now]:
                if dist + cost < distance[next]:
                    distance[next] = dist + cost
                    heapq.heappush(pq, (dist + cost, next))

        return distance


    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))

    back = dijkstra(X)
    answer = 0

    for i in range(1, N + 1):
        if X == i:
            continue

        distance = dijkstra(i)

        if distance[X] + back[i] > answer:
            answer = distance[X] + back[i]

    print(answer)

