n, m = map(int, input().split())
graph = [[int(int(1e7))] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

for i in range(1, n + 1):
    graph[i][i] = 0
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = int(1e7)
idx = 0
for i in range(1, n + 1):
    s = sum(graph[i][1:])
    if res > s:
        res = s
        idx = i

print(idx)