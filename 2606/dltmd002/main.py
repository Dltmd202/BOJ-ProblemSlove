from collections import deque

v = int(input())
e = int(input())
graph = [[]for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]
path = set()
path.add(1)
q = deque([1])
visited[1] = True
for i in range(e):
    now, will = map(int, input().split())
    graph[now].append(will)
    graph[will].append(now)

while q:
    now = q.popleft()
    for will in graph[now]:
        if not visited[will]:
            visited[will] = True
            q.append(will)
            path.add(will)

print(len(path) - 1)