import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))


def find_parent(parent: list, x: int) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent: list, a: int, b: int):
    a = find_parent(parent, parent[a])
    b = find_parent(parent, parent[b])

    if a > b:
        parent[a] = b
    else:
        parent[b] = a



n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
graph = [[0] * (n + 1)]
for i in range(n):
    graph.append([0] + list(map(int, input().split())))


travel = list(map(int, input().split()))
travel.sort()

for i in range(1, n + 1):
    for j in range(1 , n + 1):
        if graph[i][j] == 1:
            union_parent(parent, i, j)


result = set([find_parent(parent, x) for x in travel])

if len(result) == 1:
    print("YES")
else:
    print("NO")