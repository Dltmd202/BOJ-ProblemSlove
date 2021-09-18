import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
compare = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    small, big = map(int, input().split())
    compare[small][big] = 1
    compare[big][small] = -1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if compare[i][k] == 1 and compare[k][j] == 1:
                compare[i][j] = 1
            if compare[i][k] == -1 and compare[k][j] == -1:
                compare[i][j] = -1


answer = 0
for i in compare[1:]:
    result = 0
    for j in i:
        if j == 0:
            result += 1
    if result == 2:
        answer += 1

print(answer)