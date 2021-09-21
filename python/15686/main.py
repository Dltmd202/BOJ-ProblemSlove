from itertools import combinations
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chickens = []
homes = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

q = []
cnt = len(homes)
visited = set()
res = float('inf')
for combination in combinations(chickens, m):
    dist = [float('inf')] * len(homes)
    for chicken in combination:
        for home in range(len(homes)):
            h = homes[home]
            d = abs(chicken[0] - h[0]) + abs(chicken[1] - h[1])
            dist[home] = min(dist[home], d)
        res = min(res, sum(dist))
print(res)