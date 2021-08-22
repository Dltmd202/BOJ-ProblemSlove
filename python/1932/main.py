#1932
#https://www.acmicpc.net/status?user_id=bat5273&problem_id=1932&from_mine=1

n = int(input())

graph = []
answer = [[0]*n for _ in range(n)]

for i in range(n):
    data = list(map(int,input().split()))
    graph.append(data)


answer[n-1] = graph[n-1]

for i in range(n-2,-1,-1):
    for j in range(i+1):
        answer[i][j] = max(answer[i+1][j],answer[i+1][j+1]) + graph[i][j]


print(answer[0][0])