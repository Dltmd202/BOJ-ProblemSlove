import heapq
from collections import deque
import math

n , m = map(int,input().split())
graph =['.'*(m+1)]

dy = [ 0 , -1 , 0 , 1]
dx = [1 , 0 , -1 , 0]

d = deque()
water = deque()
s = deque()
rock = deque()

visit =[[0]*(m+1) for _ in range(n+1)]

wq = []

for i in range(1,n+1):
    data = '.'+input()
    for j in range(m+1):
        if data[j] == 'D':
            d.append((i,j))
        elif data[j] == '*':
            water.append((i,j))
            visit[i][j] = -1
            heapq.heappush(wq,(-1,i,j))
        elif data[j] == 'X':
            rock.append((i,j))
        elif data[j] == 'S':
            s.append((i,j))

    graph.append(data)



while wq:
    cost , y , x = heapq.heappop(wq)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 1 <= ny <= n and 1 <= nx <= m :
            if graph[ny][nx] == '.' and visit[ny][nx] == 0:
                heapq.heappush(wq,(visit[ny][nx],ny,nx))
                visit[ny][nx] = visit[y][x] -1



# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(visit[i][j], end=' ')
#     print()

dq = deque()
y , x =s.popleft()
visit[y][x] = 1
dq.append((y,x))
answer = 0
while dq:
    y ,x = dq.popleft()
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if 1 <= ny <= n and 1 <= nx <= m :
            if graph[ny][nx] == '.' and visit[ny][nx] <= 0 and visit[y][x] + 1 < abs(visit[ny][nx]):
                visit[ny][nx] = (visit[y][x] + 1)
                dq.append((ny ,nx))
            elif graph[ny][nx] == 'D' :
                visit[ny][nx] = visit[y][x] +1
                dq.append((ny,nx))

# print()
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(visit[i][j], end=' ')
#     print()

y ,x =d.popleft()

if visit[y][x] ==   0:
    print("KAKTUS")
else:
    print(visit[y][x] -1 )