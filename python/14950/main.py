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


n, m, t = map(int, input().split())


edges = []

for i in range(m):
    now, will, cost = map(int, input().split())
    edges.append([cost, now, will])


edges.sort()
parents = [i for i in range(n + 1)]
answer = 0
cnt = 0
for i in range(m):
    cost, now, will = edges[i]
    if find_parents(parents, now) != find_parents(parents, will):
        union_parents(parents, now, will)
        answer += (cost + t * cnt)
        cnt += 1

print(answer)