from collections import deque
MAX = 10001

v, e = map(int, input().split())

graph = [[] for _ in range(MAX)]
finished = [False] * MAX
parent = [0] * MAX
stack = deque()
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
        elif not finished[will]:
            result = min(result, parent[will])

    if parent[start] == result:
        scc = []
        while True:
            top = stack.pop()
            scc.append(top)
            finished[top] = True
            if top == start:
                break
        SCC.append(sorted(scc))
    return result


for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(v):
    if parent[i] == 0:
        dfs(i)
print(len(SCC) - 1)
for scc in sorted(SCC[1:]):
    print(' '.join(str(comp) for comp in scc),-1)

