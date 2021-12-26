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


g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
gate = [0] * (g + 1)
parent = [i for i in range(g + 1)]
cnt = 0

for plane in planes:
    x = find_parent(parent, plane)
    if x == 0:
        break
    union_parent(parent, x, x - 1)
    cnt += 1
print(cnt)