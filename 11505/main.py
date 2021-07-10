

n, m, k = map(int, input().split())
data = [1] * (n + 1)
tree = [1] * (n + 1)


def update(i, origin, dif):
    while i <= n:
        if not origin:
            tree[i] /= origin
            tree[i] *= dif
        else:

        i += (i & -i)


def prefix_mul(i):
    result = 1
    while i > 0:
        result *= tree[i]
        i -= (i & -i)
    return result


for i in range(1, n + 1):
    x = int(input())
    update(i, data[i], x)
    data[i] = x

for i in range(m + k):
    a, b, c = map(int, input().split())
    print(tree)
    if a == 1:
        update(b, data[b], c)
    elif a == 2:
        print(prefix_mul(c)/prefix_mul(b - 1))
