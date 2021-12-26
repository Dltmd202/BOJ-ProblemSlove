from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [input() for _ in range(n)]
visit_common = [[False] * n for _ in range(n)]
visit_non = [[False] * n for _ in range(n)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
common = 0
non = 0


def bfs(y, x, color, visit):
    q = deque()
    q.append((y, x))
    visit[y][x] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] in color and not visit[ny][nx]:
                visit[ny][nx] = True
                q.append((ny, nx))


for i in range(n):
    for j in range(n):
        if not visit_common[i][j]:
            color = [graph[i][j]]
            bfs(i, j, color, visit_common)
            common += 1
        if not visit_non[i][j]:
            if graph[i][j] == 'B':
                color = [graph[i][j]]
            else:
                color = ['R', 'G']
            bfs(i, j, color, visit_non)
            non += 1

print(common, non)
