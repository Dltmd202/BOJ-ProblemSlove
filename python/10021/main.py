import heapq
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, c = map(int, input().split())
spot = []
nodes = []
parent = [i for i in range(n)]
for i in range(n):
    spot.append(list(map(int, input().split())))
    for j in range(i):
        nodes.append(((spot[i][0] - spot[j][0])**2 + (spot[i][1] - spot[j][1])**2, i, j))

dists = 0
cnt = 0
while nodes:
    dist, start, end = heapq.heappop(nodes)
    if dist < c:
        continue
    if find_parent(parent, start) != find_parent(parent, end):
        dists += dist
        union_parent(parent, start, end)
        cnt += 1

print(-1 if cnt != n - 1 else dists)
