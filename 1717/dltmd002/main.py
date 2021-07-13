import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


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

res = []
for i in range(m):
    order, a, b = map(int, input().split())
    if order == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            res.append('YES')
        else:
            res.append('NO')

print('\n'.join(str(r) for r in res))
