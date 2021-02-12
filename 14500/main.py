import sys


input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
visit = [[False] * (m + 1) for _ in range(n + 1)]
tet = [[[0, 1], [0, 2], [-1, 1]],
       [[0, 1], [0, 2], [1, 1]],
       [[1, 0], [2, 0], [1, 1]],
       [[1, 0], [1, -1], [2, 0]]]
answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(y, x, cnt, result):
    global answer
    if cnt == 4:
        answer = max(answer, result)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not visit[ny][nx]:
            visit[ny][nx] = True
            dfs(ny, nx, cnt + 1, result + graph[ny][nx])
            visit[ny][nx] = False


def techno(y, x):
    global answer
    for i in tet:
        try:
            ans = graph[y][x] + graph[y + i[0][0]][x + i[0][1]] + graph[y + i[1][0]][x + i[1][1]] + \
                  graph[y + i[2][0]][x + i[2][1]]
        except:
            ans = 0
        answer = max(answer, ans)


for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visit[i][j] = False
        techno(i, j)

print(answer)













