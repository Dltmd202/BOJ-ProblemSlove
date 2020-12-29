#18405
#https://www.acmicpc.net/problem/18405

from collections import deque

n , k = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
q = deque()

dy = [0,-1,0,1]
dx = [1,0,-1,0]

for i in range(1,n+1):
    data = list(map(int,input().split()))
    for j in range(1,n+1):
        graph[i][j] =  data[j-1]


data = list(map(int,input().split()))
s = data[0]
target =data[1:]

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != 0 :
            q.append((i,j,0))

q =deque(sorted(q,key=lambda x:graph[x[0]][x[1]]))

cnt = 0

while q:
    nowy ,nowx,cnt = q.popleft()
    if cnt == s:
        break
    for way in range(4):
        ny = nowy +dy[way]
        nx = nowx +dx[way]
        if 1<= ny <= n and 1<= nx <= n and graph[ny][nx] == 0:
            graph[ny][nx] = graph[nowy][nowx]
            q.append((ny,nx,cnt+1))




targety,targetx = target

print(graph[targety][targetx])
