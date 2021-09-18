
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))
n , m = map(int,input().split())

visit = [[[0]*2 for _ in range(m+1)] for _ in range(n+1)]
distance = [[-1]*(m+1) for _ in range(n+1)]

dy = [ 0 , -1 , 0 , 1]
dx = [ 1 , 0 , -1 , 0]

graph =[[0]*(m+1)]


for i in range(n):
    graph.append([0]+list(map(int,input().strip())))


def bfs():
    q = deque()
    q.append((1, 1, 1))
    visit[1][1][1] = 1
    while q:

        y,x,c = q.popleft()
        # print("poped",y,x,c)
        if y == n and x == m:
            return visit[n][m][c]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # print("Time to checking",ny,nx)
            if 1<= nx <= m and 1 <= ny <= n :
                if graph[ny][nx] == 1 and c ==1:
                    visit[ny][nx][0] = visit[y][x][1] +1
                    q.append((ny,nx,0))
                elif graph[ny][nx] == 0 and visit[ny][nx][c] == 0:
                    visit[ny][nx][c] = visit[y][x][c] + 1
                    q.append((ny,nx,c))
                # else:
                    # print("Not enque",ny,nx,graph[ny][nx],visit[ny][nx][c])
            # else:
                # print("not in graph",ny,nx)
            # print(q)
    return -1

print(bfs())
