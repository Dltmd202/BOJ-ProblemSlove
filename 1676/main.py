from math import factorial
n = list(map(int, str(factorial(int(input())))))
cnt = 0
for d in reversed(n):
    if d == 0:
        cnt += 1
    else:
        print(cnt)
        break