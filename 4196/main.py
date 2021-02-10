from collections import deque
import sys
MAX = 100001
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

for tc in range(int(input())):
    e, v = map(int, input().split())

    graph = [[] for _ in range(MAX)]
    SCC = []
    stack = deque()
    id = 1
    parents = [0] * MAX
    finished = [False] * MAX
    group = [0] * MAX
    indegree = [False] * MAX

    def dfs(start):
        global id
        parents[start] = id
        id += 1
        stack.append(start)

        result = parents[start]
        for will in graph[start]:
            if parents[will] == 0:
                result = min(result, dfs(will))
            elif not finished[will]:
                result = min(result, parents[will])

        if result == parents[start]:
            scc = []
            while True:
                top = stack.pop()
                scc.append(top)
                finished[top] = True
                group[top] = len(SCC) + 1
                if top == start:
                    break
            SCC.append(scc)
        return result


    for _ in range(v):
        a, b = map(int, input().split())
        graph[a].append(b)

    for i in range(1, e + 1):
        if parents[i] == 0:
            dfs(i)

    for now in range(1, e + 1):
        for will in graph[now]:
            if group[now] != group[will]:
                indegree[group[will]] = True

    result = 0

    for i in range(1, len(SCC) + 1):
        if not indegree[i]:
            result += 1

    print(result)


