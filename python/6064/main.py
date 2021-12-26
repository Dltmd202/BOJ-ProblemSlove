from math import *
t = int(input())


def year(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


for tb in range(t):
    inputs = list(map(int, input().split()))
    print(year(*inputs))
