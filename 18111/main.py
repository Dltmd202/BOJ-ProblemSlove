import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
graph = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
answer = int(1e10)
ans_height = 0
for i in range(n):
    graph.append(list(map(int, input().split())))

for height in range(257):
    over = 0
    leak = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > height:
                over += graph[i][j] - height
            else:
                leak += height - graph[i][j]
    if leak > b + over:
        continue
    if answer >= over * 2 + leak:
        answer = min(answer, over * 2 + leak)
        ans_height = height
print(answer, ans_height)

