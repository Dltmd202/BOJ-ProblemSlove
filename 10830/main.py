
n, b = map(int, input().split())
matrix_origin = [list(map(int, input().split())) for _ in range(n)]
matrix_process = matrix_origin[:]


def square():
    sq = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                sq[i][j] += (matrix_process[i][k] * matrix_origin[k][j])
            sq[i][j] %= 1000
    return sq


for i in range(b - 1):
    matrix_process = square()

for matrix in matrix_process:
    print(' '.join(str(m) for m in matrix))