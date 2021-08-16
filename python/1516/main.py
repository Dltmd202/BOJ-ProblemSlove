from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegrees = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for v in data[1:-1]:
        graph[v].append(i)
        indegrees[i] += 1

answer = deepcopy(time)


q = deque()
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append((i, time[i]))

while q:
    now, t = q.popleft()
    for will in graph[now]:
        indegrees[will] -= 1
        answer[will] = max(answer[will], time[will] + t)
        if indegrees[will] == 0:
            q.append((will, answer[will]))

print('\n'.join(str(num) for num in answer[1:]))