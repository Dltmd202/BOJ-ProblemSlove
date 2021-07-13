import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]


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


edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort()
res = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += c

print(res)
