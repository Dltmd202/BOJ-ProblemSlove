import math

n, m = map(int, input().split())

if n >= 3 and m >= 7:
    print(m - 2)
else:
    answer = 0
    if n >= 3:
        answer = m
    elif n == 2:
        answer = m / 2
        answer = int(math.ceil(answer))
    else:
        answer = 1

    if answer >= 4:
        print(4)
    else:
        print(answer)
