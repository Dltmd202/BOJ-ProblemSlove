from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
parents = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visit[1] = True


while q:
    now = q.popleft()
    for will in graph[now]:
        if not visit[will]:
            visit[will] = True
            parents[will] = now
            q.append(will)

print('\n'.join(str(num) for num in parents[2:]))