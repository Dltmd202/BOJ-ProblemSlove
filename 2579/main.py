#2579
#https://www.acmicpc.net/problem/2579


n = int(input())


stairs =[]

for i in range(n):
    data = int(input())
    stairs.append(data)

graph =[[0]*2 for _ in range(n+1)]

def solution():
    graph[0][0] = stairs[0]
    graph[0][1] = stairs[0]
    graph[1][0] = graph[0][1] + stairs[1]
    graph[1][1] = stairs[1]

    for i in range(2,n):
        graph[i][0] = graph[i-1][1] + stairs[i]
        graph[i][1] = max(graph[i-2][0],graph[i-2][1]) + stairs[i]

    print(max(graph[n-1][0],graph[n-1][1]))

if n < 2 :
    print(stairs[0])
else:
    solution()