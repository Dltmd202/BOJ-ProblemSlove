#6086
# MAX Flow
# Edmond Karp

import sys

input = sys.stdin.readline


def CtoI(target):
    if target.isupper():
        return ord(target) - ord('A')
    else:
        return ord(target) - ord('a') + 26


from collections import deque

INF = int(1e9)
MAX = 53

result = 0
capacity = [[0] * MAX for _ in range(MAX)]
flow = [[0] * MAX for _ in range(MAX)]
graph = [[] for _ in range(MAX)]
distance = [-1] * MAX


def maxFlow(start, end):
    result = 0
    # print(start,end)
    while True:
        for i in range(MAX): distance[i] = -1
        q = deque()
        q.append(start)
        while q and distance[end] == -1:
            now = q.popleft()
            for will in graph[now]:
                if capacity[now][will] - flow[now][will] > 0 and distance[will] == -1:
                    q.append(will)
                    distance[will] = now
                    # print(will , distance[will])
                    if will == end: break
        # print(distance)

        if distance[end] == -1: break
        minflow = INF

        i = end
        while i != start:
            minflow = min(minflow, capacity[distance[i]][i] - flow[distance[i]][i])
            i = distance[i]

        i = end
        while i != start:
            flow[distance[i]][i] += minflow
            flow[i][distance[i]] -= minflow
            i = distance[i]
        result += minflow

    return result


n = int(input())
for i in range(n):
    a, b, c = list(input().split())
    a = CtoI(a)
    b = CtoI(b)
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b] += int(c)
    capacity[b][a] += int(c)

print(maxFlow(CtoI('A'), CtoI('Z')))

