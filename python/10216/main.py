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


for tc in range(int(input())):
    n = int(input())
    parent = [i for i in range(n)]
    answer = n
    y_pos = [0] * n
    x_pos = [0] * n
    radius = [0] * n

    for i in range(n):
        y, x, r = map(int, input().split())
        y_pos[i] = y
        x_pos[i] = x
        radius[i] = r

    for i in range(n):
        for j in range(i + 1, n):
            y_dif = y_pos[i] - y_pos[j]
            x_dif = x_pos[i] - x_pos[j]
            r = radius[i] + radius[j]

            if y_dif ** 2 + x_dif ** 2 <= r * r:
                if find_parent(parent, i) != find_parent(parent, j):
                    union_parent(parent, i, j)
                    answer -= 1
    print(answer)