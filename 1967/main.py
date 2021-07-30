import sys
sys.setrecursionlimit(100000)
inf: int = int(1e9)

n: int = int(input())
graph: list = [[]for _ in range(n + 1)]
visit: list = [False] * (n + 1)
res: int = 0

for i in range(n - 1):
    start, dest, dist = map(int, input().split())
    graph[start].append([dist, dest])


def dfs(start: int) -> int:
    global res
    left, right = 0, 0
    visit[start] = True
    for cost, will in graph[start]:
        if not visit[will]:
            buf = dfs(will)
            if left < buf + cost:
                right = left
                left = buf + cost
            elif right < buf + cost:
                right = buf + cost
    res = max(res, left + right)
    return left


dfs(1)
print(res)