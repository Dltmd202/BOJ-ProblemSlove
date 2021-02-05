import sys
sys.setrecursionlimit(int(1e9))

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
depth = [0] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, d):
    visit[x] = True
    depth[x] = d

    for y  in graph[x]:
        if visit[y]:
            continue
        parent[y] = x
        dfs(y, d + 1)


def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


dfs(1, 0)
m = int(input())
for i in range(m):
    a, b = map(int,input().split())
    print(lca(a, b))
