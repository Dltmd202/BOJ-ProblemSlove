from collections import defaultdict
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


n, m, k = map(int, input().split())
cost = [0] + list(map(int,  input().split()))
parents = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)

group = defaultdict(list)
roots = []
for i in range(1, n + 1):
    if not group[find_parent(parents, i)]:
        roots.append(i)
    group[find_parent(parents, i)].append(i)

answer = 0
for root in roots:
    c = int(1e9)
    for member in group[root]:
        c = min(c, cost[member])
    answer += c

if answer > k:
    print("Oh no")
else:
    print(answer)