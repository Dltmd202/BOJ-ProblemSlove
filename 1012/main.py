from collections import deque

t = int(input())
answer = []



def solution():
    m , n , k = map(int,input().split())
    graph = [[0]*(m) for _ in range(n)]

    dy = [0 , -1 , 0 , 1]
    dx = [1 , 0 , -1 , 0]

    for i in range(k):
        x ,y = map(int,input().split())
        graph[y][x] = 1

    q = deque()
    cnt = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i,j))
                cnt += 1
                graph[i][j] = cnt
                while q:
                    y , x =q.popleft()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                            graph[ny][nx] = cnt
                            q.append((ny,nx))

    return cnt-1

for i in range(t):
    answer.append(solution())

for i in answer:
    print(i)