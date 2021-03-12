from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
t = [0] * (n + 1)
answer = [0] * (n + 1)
ind = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    t[i] = data[0]
    for j in range(2, len(data)):
        graph[data[j]].append(i)
        ind[i] += 1

q = deque()
for i in range(1, n + 1):
    if ind[i] == 0:
        q.append((i, t[i]))
        answer[i] = t[i]

while q:
    now, cost = q.popleft()
    for will in graph[now]:
        ind[will] -= 1
        answer[will] = max(answer[will], answer[now] + t[will])
        if ind[will] == 0:
            q.append((will, cost + t[will]))

print(max(answer[1:]))