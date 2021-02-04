from copy import deepcopy
from collections import deque

n = int(input())
graph = [[0] * (n + 1)]
visit = [[False] * (n + 1) for _ in range(n + 1)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for i in range(n):
    line = list(map(int, input().split()))
    graph.append([0] + line)

def bfs(i: int, j: int, pivot: int, visit):
    q = deque()
    q.append((i, j))
    visit[i][j] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 1 <= ny <= n and 1 <= nx <= n and graph[ny][nx] > pivot and visit[ny][nx] == False:
                visit[ny][nx] = True
                q.append((ny, nx))
    return visit

answer = 1
for hight in range(1, 101):
    visit_rep = deepcopy(visit)
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > hight and visit_rep[i][j] == False:
                cnt += 1
                bfs(i, j, hight, visit_rep)
    answer = max(answer, cnt)
print(answer)