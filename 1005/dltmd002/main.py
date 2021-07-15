import sys
from collections import deque
input = sys.stdin.readline
tb = int(input())
inf = int(1e9)

for t in range(tb):
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    costs = [0] * (n + 1)
    ind = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    q = deque()

    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        ind[y] += 1
    dest = int(input())
    for i in range(1, n + 1):
        if ind[i] == 0:
            q.append(i)
            costs[i] = times[i]

    while q:
        now = q.popleft()
        for will in graph[now]:
            costs[will] = max(costs[now], costs[will])
            ind[will] -= 1
            if ind[will] == 0:
                q.append(will)
                costs[will] = times[will] + costs[will]

    print(costs[dest])