from collections import deque

n, k = map(int, input().split())
max_val = int(1e5)
visited = [-1] * (max_val + 1)
q = deque()
q.append(n)
visited[n] = 0

while q:
    now = q.popleft()
    if now == k:
        print(visited[k])
        break
    if 0 <= now + 1 <= max_val and visited[now + 1] == - 1:
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)
    if 0 <= now - 1 <= max_val and visited[now - 1] == - 1:
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)
    if 0 <= now * 2 <= max_val and visited[now * 2] == - 1:
        visited[now * 2] = visited[now] + 1
        q.append(now * 2)
