import math
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
f = 0
b = 0

for i in range(n):
    f += (graph[i][0] * graph[(i + 1) % n][1])
    b += (graph[(i + 1) % n][0] * graph[i][1])


print(round(abs(b-f)/2, 1))
