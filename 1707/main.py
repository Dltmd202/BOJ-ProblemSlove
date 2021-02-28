from collections import deque
import sys
input = sys.stdin.readline


for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for i in range(e):
        now, will = map(int, input().split())
        graph[now].append(will)
        graph[will].append(now)
    result = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            visited[i] = 1
            q = deque([i])
            while q:
                now = q.popleft()
                for will in graph[now]:
                    if visited[will] == 0:
                        visited[will] = -1 * visited[now]
                        q.append(will)
                    else:
                        if visited[will] == visited[now]:
                            result = False
                            break
            if not result:
                break
    print("YES" if result else "NO")
