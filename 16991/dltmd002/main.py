import sys
input = sys.stdin.readline
n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]
w = [[0] * (n + 1) for _ in range(n + 1)]


for i in range(n):
    for j in range(i, n):
        a, b = dots[i], dots[j]
        dist = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
        w[i][j], w[j][i] = dist, dist


def isIn(a, i):
    if a & (1 << (i - 1)):
        return True
    else:
        return False


def diff(a, i):
    return a & ~(1 << (i - 1))


def count(a, n):
    cnt = 0
    for i in range(n):
        if a & (1 << i):
            cnt += 1
    return cnt


def minimum(dp, i, a):
    min_val = float('inf')
    min_j = 1
    for j in range(1, n):
        if isIn(a, j):
            m = w[i][j] + dp[j][diff(a, j)]
            min_val = min(min_val, m)
    return min_val


def travel():
    global n
    size = 1 << (n - 1)
    dp = [[0.] * size for _ in range(n)]
    for i in range(n):
        dp[i][0] = w[i][0]
    for k in range(1, n):
        for a in range(1, size):
            if count(a, n) == k:
                for i in range(1, n):
                    if not isIn(a, i):
                        dp[i][a] = minimum(dp, i, a)

    a = size - 1
    return minimum(dp, 0, a)


print(travel())
