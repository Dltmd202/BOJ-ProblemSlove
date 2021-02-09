from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
MAX = 10001

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
stack = deque()
finish = [False] * MAX
parent = [0] * MAX
SCC = []
id = 1


def dfs(start):
    global id
    parent[start] = id
    id += 1
    stack.append(start)

    result = parent[start]
    for will in graph[start]:
        if parent[will] == 0:
            result = min(result, dfs(will))
        elif not finish[will]:
            result = min(result, parent[will])

    if result == parent[start]:
        scc = []
        while True:
            top = stack.pop()
            scc.append(top)
            finish[top] = True
            if top == start:
                break
        SCC.append(sorted(scc))
    return result

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)


for i in range(v):
    if parent[i] == 0:
        dfs(i)
SCC.sort()
print(len(SCC) - 1)

for scc in SCC[1:]:
    for comp in scc:
        print(comp, end=' ')
    print(-1)