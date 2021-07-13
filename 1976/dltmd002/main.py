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


for i in range(1, n + 1):
    line = [0] + list(map(int, input().split()))
    for j in range(1, len(line)):
        if line[j] == 1:
            union(i, j)

trav = list(map(int, input().split()))
res = True

for t in trav:
    if find(trav[0]) != find(t):
        res = False
        break

print('YES' if res else 'NO')