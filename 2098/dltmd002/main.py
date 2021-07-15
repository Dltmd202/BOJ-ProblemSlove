import sys
input = sys.stdin.readline

n = int(input())
w = [[0] + list(map(int, input().split())) for _ in range(n)]
inf = int(1e12)
dp = [[0] * (1 << n - 1) for _ in range(n)]


def isIn(a, i):
    if (a & (1 << (i - 2))) != 0:
        return True
    else:
        return False


def diff(a, j):
    return a & ~(1 << (j - 2))


def count(a, n):
    cnt = 0
    for i in range(2, n + 2):
        if a & (1 << (i - 2)):
            cnt += 1
    return cnt


def minimum(d, i, a):
    min_val = inf
    min_j = 1
    n = len(w) - 1
    for j in range(2, n + 1):
        if isIn(a, j):
            m = w[i][j] + d[j][diff(a, j)]
            if min_val > m:
                min_val = m
                min_j = j
    return min_val, min_j


def travel():
    n = len(w) - 1
    size = 1 << (n - 1)
    d = [[0] * size for _ in range(n + 1)]
    p = [[0] * size for _ in range(n + 1)]
    for i in range(2, n + 1):
        d[i][0] = w[i][1]
    for k in range(1, n - 1):
        for a in range(1, size):
            if count(a, n) == k:
                for i in range(2, n + 1):
                    if not isIn(a, i):
                        d[i][a], p[i][a] = minimum(d, i, a)

    a = size - 1
    d[1][a], p[i][a] = minimum(d, 1, a)
    return d, p


w = [[0 for i in range(n + 1)]] + w
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not w[i][j]:
            w[i][j] = inf

d, p = travel()
res = d[1][(1 << (n - 1)) - 1]
print(res if res <= inf else 0)