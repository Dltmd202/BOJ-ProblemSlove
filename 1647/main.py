import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
edges = []
for _ in range(m):
    now, will, cost = map(int, input().split())
    edges.append((cost, now, will))

edges.sort()
ways = []
parent = [i for i in range(n + 1)]

for edge in edges:
    cost, now, will = edge
    if find_parent(parent, now) != find_parent(parent, will):
        union_parent(parent, now, will)
        ways.append(cost)

ways.sort(reverse=True)
print(sum(ways[1:]))