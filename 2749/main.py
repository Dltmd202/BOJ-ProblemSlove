from copy import deepcopy
MOD = 1_000_000


def dot(mat1, mat2):
    n1, m1 = len(mat1), len(mat1[0])
    n2, m2 = len(mat2), len(mat2[0])
    res = [[0] * m2 for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            buf = 0
            for k in range(m1):
                buf += (mat1[i][k] * mat2[k][j])
            res[i][j] = buf % MOD
    return res


def pow(matrix, a):
    if a == 1:
        return matrix
    else:
        ret = pow(matrix, a // 2)
        pow_matrix = dot(ret, ret)
        if a % 2 == 0:
            return pow_matrix
        else:
            return dot(pow_matrix, matrix)


def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    res_matrix = pow([[1, 1], [1, 0]], n - 1)
    res = dot(res_matrix, [[1], [0]])
    return res[0][0]


n = int(input())
print(solution(n))