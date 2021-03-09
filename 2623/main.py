import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    data = list(map(int, input().split()))[1:]
    for i in range(len(data) - 1):
        graph[data[i]].append(data[i + 1])
        ind[data[i + 1]] += 1

q = deque()

for i in range(1, n + 1):
    if ind[i] == 0:
        q.append(i)

answer = []

while q:
    now = q.popleft()
    answer.append(now)
    for will in graph[now]:
        ind[will] -= 1
        if ind[will] == 0:
            q.append(will)

if sum(ind):
    print(0)
else:
    print('\n'.join(str(i) for i in answer))