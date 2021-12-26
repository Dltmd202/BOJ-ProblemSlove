

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


for tc in range(int(input())):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    answer = 0
    query = []
    for i in range(m):
        f, b = map(int, input().split())
        query.append((f, b))
    for i in range(m):
        f, b = query.pop()
        bp = find_parent(parent, b)
        if bp >= f:
            union_parent(parent, bp, bp - 1)
            answer += 1
        else:
            break
    print(answer)
