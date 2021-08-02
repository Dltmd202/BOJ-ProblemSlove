import sys
input = sys.stdin.readline
MOD = 1_000


def dot(mat1, mat2):
    n1, m1 = len(mat1), len(mat1[0])
    n2, m2 = len(mat2), len(mat2[0])
    ret = [[0] * m2 for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            buf = 0
            for k in range(m1):
                buf += (mat1[i][k] * mat2[k][j])
            ret[i][j] = buf % MOD
    return ret


def pow(matrix, a):
    if a == 1:
        return matrix

    ret = pow(matrix, a//2)
    ret = dot(ret, ret)
    if a % 2:
        return dot(ret, matrix)
    else:
        return ret


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
sqd = pow(matrix, b)
print('\n'.join(' '.join(str(c % MOD) for c in l) for l in sqd))