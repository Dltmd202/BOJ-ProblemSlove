import sys
input = sys.stdin.readline
inf = int(1e9)
t = int(input())

for tc in range(t):
    n, m, w = map(int, input().split())
    graph = [[]for _ in range(n + 1)]
    distance = [inf] * (n + 1)
    for i in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([t, e])
        graph[e].append([t, s])
    for i in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([-t, e])


    def bf():
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for cost, will in graph[j]:
                    if distance[will] > cost + distance[j]:
                        distance[will] = cost + distance[j]
                        if i == n:
                            return True
        return False

    print('YES' if bf() else 'NO')
