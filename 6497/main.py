import sys
input = sys.stdin.readline


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    answer = 0
    max_use = 0
    parent = [i for i in range(n + 1)]
    edges = []
    for i in range(m):
        x, y, z = map(int, input().split())
        max_use += z
        edges.append((z, x, y))
    edges.sort()
    for i in range(m):
        z, x, y = edges[i]
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            answer += z
    print(max_use - answer)