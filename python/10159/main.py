import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    big, small = map(int, input().split())
    graph[big][small] = 1
    graph[small][big] = -1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
            if graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1

answer = [0] * (n + 1)

for line in range(len(graph)):
    cnt = 0
    for i in graph[line]:
        if i == 0:
            cnt += 1
    answer[line] = cnt -2

print('\n'.join(str(i) for i in answer[1:]))