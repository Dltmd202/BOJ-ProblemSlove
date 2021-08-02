

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]


def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]


cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            cnt += 1

result = True
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            result = False

if result:
    print(cnt)
else:
    print(-1)

