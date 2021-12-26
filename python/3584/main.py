from collections import deque
from math import log2, ceil

for tc in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    log_2 = int(ceil(log2(n)))
    parent = [[0] * log_2 for _ in range(n + 1)]
    depth = [0] * (n + 1)
    root = -1
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        parent[b][0] = a
    start, end = map(int, input().split())
    for i in range(1, n + 1):
        if parent[i][0] == 0:
            root = i
            break
    visit[root] = True
    q = deque()
    q.append(root)
    while q:
        now = q.popleft()
        for will in graph[now]:
            if not visit[will]:
                visit[will] = True
                depth[will] = depth[now] + 1
                q.append(will)

    for i in range(1, log_2):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]
    if depth[start] > depth[end]:
        start, end = end, start
    for i in range(log_2 - 1, -1, -1):
        if depth[end] - depth[start] >= (1 << i):
            end = parent[end][i]

    if start == end:
        print(start)
        continue

    for i in range(log_2 - 1, -1, -1):
        if parent[start][i] != parent[end][i]:
            start = parent[start][i]
            end = parent[end][i]
    print(parent[start][0])

