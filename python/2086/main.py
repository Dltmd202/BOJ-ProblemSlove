import sys
sys.setrecursionlimit(int(1e5) * 3)
MOD = 1_000_000_000


def dot(a, b):
    n, m = len(a), len(b[0])
    new = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(n):
                new[i][j] += (a[i][k] * b[k][j])
            new[i][j] %= MOD
    return new


def pow(matrix, a):
    if a == 1:
        return matrix
    ret = pow(matrix, a // 2)
    pow_matrix = dot(ret, ret)
    if a % 2 == 0:
        return pow_matrix
    else:
        return dot(pow_matrix, matrix)


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    temp = [[1, 1], [1, 0]]
    ans = [[1], [1]]
    res_matrix = pow2(temp, n - 2)
    res = dot(res_matrix, ans)
    return res[0][0]


def pow2(matrix, a):
    n = len(matrix)
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    while a > 0:
        if a % 2:
            ret = dot(matrix, ret)
        matrix = dot(matrix, matrix)
        a //= 2
    return ret


a, b = map(int, input().split())
ra, rb = fibo(a + 1), fibo(b + 2)
print((rb % MOD - ra % MOD + MOD) % MOD)