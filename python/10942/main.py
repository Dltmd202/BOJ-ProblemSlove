import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if data[i] == data[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, n):
    for j in range(n - i):
        if data[j] == data[j + i] and dp[j + 1][j + i - 1] == 1:
            dp[j][i + j] = 1

answer = []
for tb in range(int(input())):
    s, e = map(int, input().split())
    answer.append(dp[s-1][e-1])
print('\n'.join(str(i) for i in answer))
