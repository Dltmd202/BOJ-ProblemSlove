import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


edges = []
for i in range(e):
    now, will, cost = map(int, input().split())
    edges.append([cost, now, will])

edges.sort()
res = 0
for edge in edges:
    cost, now, will = edge
    if find_parent(now) != find_parent(will):
        res += cost
        union_parent(now, will)

print(res)