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


n = int(input())
m = int(input())
edges = []
parent = [0] * (n + 1)
for i in range(1, n + 1): parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

answer = 0
for edge in edges:
    cost, now, will = edge
    if find_parent(parent, now) != find_parent(parent, will):
        union_parent(parent, now, will)
        answer += cost

print(answer)
