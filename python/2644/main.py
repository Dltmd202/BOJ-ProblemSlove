from collections import deque

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n + 1)]
m = int(input())
for i in range(m):
    now, will = map(int, input().split())
    graph[now].append(will)
    graph[will].append(now)

q = deque()
visited = [False] * (n + 1)
q.append((a, 0))


def bfs():
    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt
        for will in graph[now]:
            if not visited[will]:
                q.append((will, cnt + 1))
                visited[will] = True
    return -1


print(bfs())