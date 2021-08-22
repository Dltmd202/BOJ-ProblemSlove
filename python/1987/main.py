import sys
input = sys.stdin.readline

c, r = map(int, input().split())
graph = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for i in range(c):
    graph.append(input())

visit = [False] * 27
answer = 0


def c_to_i(y, x):
    return ord(graph[y][x]) - ord('A')


def dfs(y, x, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < c and 0 <= nx < r:
            num = c_to_i(ny, nx)
            if not visit[num]:
                visit[num] = True
                dfs(ny, nx, cnt + 1)
                visit[num] = False


visit[c_to_i(0, 0)] = True
dfs(0, 0, 1)
print(answer)