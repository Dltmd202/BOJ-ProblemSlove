import math
n = int(input())
res = 4

for i in range(int(n ** 0.5), int((n // 4) ** 0.5), -1):
    if i*i == n:
        res = 1
        break
    else:
        buf = n - i*i
        for j in range(int(buf**0.5), int((buf//3)**0.5), -1):
            if i*i + j*j == n:
                res = min(res, 2)
                continue
            else:
                buf = n - i*i - j*j
                for k in range(int(buf**0.5), int((buf//2)**0.5), -1):
                    if n == i*i + j*j + k*k:
                        res = min(res, 3)
print(res)