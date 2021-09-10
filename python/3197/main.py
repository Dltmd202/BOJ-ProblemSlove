from collections import deque
import sys
input = sys.stdin.readline
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def waters():
    while water:
        y, x = water.popleft()
        if graph[y][x] == 'X':
            graph[y][x] = '.'
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if not is_melted[ny][nx]:
                    if graph[ny][nx] == 'X':
                        water_temp.append((ny, nx))
                    else:
                        water.append((ny, nx))
                    is_melted[ny][nx] = True


def bfs():
    while q:
        y, x = q.popleft()
        if y == swan[1][0] and x == swan[1][1]:
            return True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if not visited[ny][nx]:
                    if graph[ny][nx] != 'X':
                        q.append((ny, nx))
                    else:
                        q_temp.append((ny, nx))
                    visited[ny][nx] = True
    return False


r, c = map(int, input().split())
water, water_temp = deque(), deque()
q, q_temp = deque(), deque()
visited = [[False] * c for _ in range(r)]
is_melted = [[False] * c for _ in range(r)]
graph = []
swan = []

for i in range(r):
    row = list(input().strip())
    graph.append(row)
    for j in range(c):
        if graph[i][j] == 'L':
            swan.append((i, j))
            water.append((i, j))
            is_melted[i][j] = True
        elif graph[i][j] == '.':
            water.append((i, j))
            is_melted[i][j] = True

q.append(swan[0])
visited[swan[0][0]][swan[0][1]] = True

cnt = 0
while True:
    waters()
    if bfs():
        print(cnt)
        break
    q, water = q_temp, water_temp
    q_temp, water_temp = deque(), deque()
    cnt += 1
