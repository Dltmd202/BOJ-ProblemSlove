import sys
input = sys.stdin.readline


def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]


def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


n, m = map(int, input().split())
school = [' '] + list(input().split())
parents = [i for i in range(n + 1)]
edges = []
selected = [0] * (n + 1)

for i in range(m):
    now, will, cost = map(int, input().split())
    edges.append((cost, now, will))

answer = 0
edges.sort(key=lambda x: x[0])
for i in range(m):
    cost, now, will = edges[i]
    if find_parents(parents, now) != find_parents(parents, will) and school[now] != school[will]:
        union_parents(parents, now, will)
        selected[now] = 1
        selected[will] = 1
        answer += cost

result = True

if sum(selected) == n:
    print(answer)
else:
    print(-1)