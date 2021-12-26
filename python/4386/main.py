from math import sqrt
import sys
import heapq
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
q = []


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


stars = [list(map(float, input().split())) for _ in range(n)]
edges = dict()

for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        a, b = stars[i], stars[j]
        dist = round(sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2), 5)
        heapq.heappush(q, (dist, (i, j)))


res = 0.
while q:
    dist, (a, b) = heapq.heappop(q)
    if find(a) != find(b):
        union(a, b)
        res += dist

print(round(res, 2))
