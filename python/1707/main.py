from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    def bfs(start):
        visited[start] = 1
        q = deque()
        q.append(start)
        while q:
            now = q.popleft()
            for i in graph[now]:
                if visited[i] == 0:
                    visited[i] = -visited[now]
                    q.append(i)
                else:
                    if visited[i] == visited[now]:
                        return False
        return True

    v, e = map(int, input().split())
    graph = [[] for i in range(v + 1)]
    visited = [0 for i in range(v + 1)]
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = True
    for k in range(1, v + 1):
        if visited[k] == 0:
            if not bfs(k):
                res = False
                break
    print("YES"if res else "NO")
