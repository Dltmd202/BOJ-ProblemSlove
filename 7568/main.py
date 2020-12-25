#7568
#https://www.acmicpc.net/problem/7568


n = int(input())

graph =[]
grade = [1]*n

for i in range(n):
    w , t = map(int,input().split())
    graph.append((w,t))

for i in range(n):
    w,t = graph[i]
    for j in range(n):
        if not i == j :
            weight , tall = graph[j]
            if w < weight and t < tall :
                grade[i] += 1

for i in grade:
    print(i, end=' ')
