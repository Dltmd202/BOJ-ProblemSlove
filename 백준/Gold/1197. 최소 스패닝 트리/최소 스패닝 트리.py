import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b :
        parent[a] = b
    else:
        parent[b] = a


if __name__ == '__main__':
    v, e = map(int, input().split())
    parents = [i for i in range(v + 1)]
    edges = []

    for i in range(e):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    heapq.heapify(edges)

    cost = 0

    while edges:
        c, a, b = heapq.heappop(edges)

        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            cost += c

    print(cost)
