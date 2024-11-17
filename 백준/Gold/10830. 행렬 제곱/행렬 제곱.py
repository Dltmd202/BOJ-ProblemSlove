MOD = 1_000

if __name__ == '__main__':
    n, b = map(int, input().split())
    a = [list(map(lambda x: int(x) % 1_000, input().split())) for _ in range(n)]

    def mul(a, b):
        h = len(a)
        w = len(b[0])
        rotated = [list(x) for x in zip(*b)]
        new_matrix = [[0 for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                val = 0
                for x, y in zip(a[i], rotated[j]):
                    val += x * y
                    val %= MOD
                new_matrix[i][j] = val
        return new_matrix


    def pow2(a):
        return mul(a, a)


    def pow(a, n):
        if n == 1:
            return a
        elif n == 2:
            return pow2(a)

        time = n // 2
        tmp = pow(a, time)
        tmp = mul(tmp, tmp)

        if n % 2 != 0:
            tmp = mul(a, tmp)
        return tmp


    answer = pow(a, b)
    for i in range(n):
        print(' '.join(str(d) for d in answer[i]))
