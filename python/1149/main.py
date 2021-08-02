#1149.py
#https://www.acmicpc.net/problem/1149
#O(N)


n = int(input())
INF = int(1e9)

#dp 테이블 초기화
d = [[INF]*4 for _ in range(n + 1)]
#graph 초기화
graph = [[] for _ in range(n + 1)]


for i in range(1, n + 1):
    graph[i].append(0)
    graph[i] = list(map(int, input().split()))

d[1] =graph[1]

for i in range(2,n+1):
    for j in range(3):
        for k in range(3):
            if not j == k :
                d[i][j] = min( d[i][j] , graph[i][j] + d[i-1][k] )

print(min( d[n] ))