import heapq


def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a


if __name__ == '__main__':
    N = int(input())
    edges = []
    parents = [i for i in range(N + 1)]

    for i in range(N):
        cost = int(input())
        edges.append((cost, 0, i + 1))

    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if i == j:
                continue
            edges.append((line[j], i + 1, j + 1))

    heapq.heapify(edges)
    answer = 0

    while edges:
        c, a, b = heapq.heappop(edges)
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            answer += c

    print(answer)
