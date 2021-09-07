from collections import defaultdict, deque
import sys
input = sys.stdin.readline
INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = INF


def getKey(char: str):
    return ord(char) - ord('a')


def getDoor(char: str):
    return ord(char) - ord('A')


n, m = map(int, input().split())
graph = []
visit = [[[False] * (1 << 6) for i in range(m)] for _ in range(n)]
q = deque()

for i in range(n):
    line = list(input().strip())
    for j in range(len(line)):
        if line[j] == '0':
            q.append((i, j, 0, 0))
            visit[i][j][0] = 1
            line[j] = '.'
    graph.append(line)
res = False


def search():
    while q:
        y, x, v, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] != "#" and not visit[ny][nx][v]:
                    if graph[ny][nx] == '.':
                        visit[ny][nx][v] = True
                        q.append((ny, nx, v, cnt + 1))
                    elif graph[ny][nx] == '1':
                        return cnt + 1
                    else:
                        if graph[ny][nx].isupper():
                            if v & (1 << getDoor(graph[ny][nx])):
                                visit[ny][nx][v] = True
                                q.append((ny, nx, v, cnt + 1))
                        else:
                            nv = v | (1 << getKey(graph[ny][nx]))
                            if not visit[ny][nx][nv]:
                                visit[ny][nx][nv] = True
                                q.append((ny, nx, nv, cnt + 1))
    return -1


print(search())