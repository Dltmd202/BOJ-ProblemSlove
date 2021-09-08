import math
import sys
input = sys.stdin.readline

def dfs(now, v):
    visited[now] = True
    val[now] *= v
    for will in graph[now]:
        if not visited[will]:
            dfs(will, v)


n = int(input())
graph = [[] for _ in range(n)]
val = [1] * n
for i in range(n - 1):
    a, b, p, q = map(int, input().split())
    g = int(math.gcd(val[a], val[b]))
    a_, b_ = val[b] // g * p, val[a] // g * q
    g = int(math.gcd(a_, b_))
    visited = [False] * n
    dfs(a, a_ // g)
    dfs(b, b_ // g)
    graph[a].append(b)
    graph[b].append(a)

print(*val)