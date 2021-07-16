factorial = [1] * 1001
factorial[0] = 1
factorial[1] = 1
factorial[2] = 2
for i in range(3, 1001):
    factorial[i] = factorial[i - 1] * i


n, k = map(int, input().split())
print((factorial[n] // (factorial[n - k] * factorial[k])) % 10007)
