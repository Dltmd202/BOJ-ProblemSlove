from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
visit = [False] * (n + 1)
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for v in range(1, len(data) - 1, 2):
        graph[i].append((data[v], data[v + 1]))

q = deque()
q.append((1, 0))
visit[1] = True
answer = 0


while q:
    now, length = q.popleft()
    answer = max(answer, length)
    for v, cost in graph[now]:
        if not visit[v]:
            visit[v] = True
            q.append((v, length + cost))

print(answer)
