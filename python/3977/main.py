from collections import deque
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    SCC = []
    stack = deque()
    visit = [False] * n
    finish = [False] * n
    id = 0
    group = [-1] * n
    parent = [-1] * n
    indegree = [0] * n
    start_area = []
    answer = []

    def dfs(start):
        global id
        parent[start] = id
        id += 1
        stack.append(start)

        result = parent[start]
        for will in graph[start]:
            if not visit[will]:
                if parent[will] == -1:
                    result = min(result, dfs(will))
                elif not finish[will]:
                    result = min(result, parent[will])

        if result == parent[start]:
            scc = []
            while True:
                top = stack.pop()
                scc.append(top)
                parent[top] = result
                finish[top] = True
                group[top] = len(SCC)
                if top == start:
                    break
            SCC.append(scc)
        return result

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    if tc != t - 1:
        input()

    for i in range(n):
        if parent[i] == -1:
            dfs(i)

    for now in range(n):
        for will in graph[now]:
            if group[now] != group[will]:
                indegree[group[will]] += 1
    for i in range(len(SCC)):
        if indegree[i] == 0:
            start_area.append(i)

    if len(start_area) == 1:
        print('\n'.join(str(num) for num in sorted(SCC[start_area[0]])))
    else:
        print('Confused')
    print()

