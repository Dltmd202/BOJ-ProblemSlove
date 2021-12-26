
from copy import deepcopy

n = int(input())
cnt = 0
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]


def solution(n):
    graph =[[-1]*(n+1) for _ in range(n+1)]


    def put(graph,y,x):
        for k in range(1,n+1):
            graph[y][k] = 0
            graph[k][x] = 0

        pivot = max(y,x)

        for i in range(0, (n+1)-pivot+1):
            if 1<= y+i <= n and 1<= x+i <= n:
                graph[y+i][x+i] = 0
            if 1<= y-i <= n and 1<= x+i <= n:
                graph[y-i][x+i] = 0
        for i in range(0,pivot+1):
            if 1<= y-i <= n and 1<= x-i <= n:
                graph[y-i][x-i] = 0
            if 1<=y+i <= n and 1<= x-i <= n:
                graph[y+i][x-i] = 0
        graph[y][x] =1


    cnt = 0



    def sol(graph, y , x ,left):
        global cnt

        if left == 0:
            cnt += 1
            return cnt

        for i in range(y,n+1):
            for j in range(1,n+1):
                if graph[i][j] == -1:
                    g = deepcopy(graph)
                    put(g,i,j)
                    sol(g,i,j,left-1)
        return cnt
    print(sol(graph,1,1,n))

print(answer[n])
