#2775
#https://www.acmicpc.net/problem/2775
#O(case)

case = int(input())

graph = [[0]*15 for _ in range(15)]
for i in range(1,15) :graph[0][i] = i

for i in range(1,15):
    for j in range(1,15):
        for k in range(1,j+1):
            graph[i][j] += graph[i-1][k]




def solution():
    k = int(input())
    n = int(input())
    return graph[k][n]


answer = []

for i in range(case):
    answer.append(solution())


for i in answer:
    print(i)
