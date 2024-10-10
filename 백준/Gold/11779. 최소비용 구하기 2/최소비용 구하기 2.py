import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))

    start, target = map(int, input().split())

    distance = [INF for _ in range(n + 1)]
    distance[start] = 0

    pq = []
    pq.append((0, start, [start]))
    answer = INF
    ans_path = ()

    while pq:
        cost, now, path = heapq.heappop(pq)

        if distance[now] < cost:
            continue

        for c, will in graph[now]:
            if cost + c < distance[will]:
                distance[will] = cost + c
                pq.append((cost + c, will, (*path, will)))

                if will == target:
                    ans_path = (*path, will)

    print(distance[target])
    print(len(ans_path))
    print(' '.join(str(i) for i in ans_path))
