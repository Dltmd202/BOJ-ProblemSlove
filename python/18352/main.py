#18352
#https://www.acmicpc.net/problem/18352
#O(N+M)

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)

for i in range(m):
    now, to = map(int, input().split())
    graph[now].append(to)


def bfs(graph, start):
    q = deque([start])
    distance[start] = 0
    while q:
        now = q.popleft()
        for will in graph[now]:
            if distance[will] == -1:
                q.append(will)
                distance[will] = (distance[now] + 1)


bfs(graph, x)

if k not in distance:
    print(-1)
else:
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)





