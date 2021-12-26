import sys

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dy = [0, -1, 0, 1]
dx = [1, 0 , -1, 0]
red, blue, hole = [], [], []
red_visit = [[False] * m for _ in range(n)]
blue_visit = [[False] * m for _ in range(n)]
visit = set()
answer = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            red = [i, j]
            red_visit[i][j] = True
        elif graph[i][j] == 'B':
            blue = [i, j]
            blue_visit[i][j] = True
        elif graph[i][j] == 'O':
            hole = [i, j]
visit.add((*red, *blue))
print(visit)


def dfs(cnt, red, blue):
    global answer
    for i in range(4):
        ry, rx = red
        by, bx = blue
        while 0 <= ry + dy[i] < n and 0 <= rx + dx[i] < m:
            ry = ry + dy[i]
            rx = rx + dx[i]
            if ry == hole[0] and rx == hole[1]:
                answer = max(answer, cnt + 1)
                return
        while 0 <= by + dy[i] < n and 0 <= bx + dx[i] < m and [by, bx] != hole:
            by = by + dy[i]
            bx = bx + dx[i]
            if by == hole[0] and bx == hole[1]:
                return
        nred = [ry, rx]
        nblue = [by, bx]
        if (*nred, *nblue) not in visit:
            visit.add((*nred, *nblue))

            dfs(cnt + 1, nred, nblue)

dfs(0, red, blue)
print(answer)
