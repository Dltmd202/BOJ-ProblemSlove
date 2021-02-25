import sys
input = sys.stdin.readline

MAX = int(1e9)
dp = [0] * 100
dp[1] = 1
i = 2
while i < 100 and dp[i - 1] <= MAX:
    dp[i] = dp[i - 1] + dp[i - 2]
    i += 1
i -= 1
for tc in range(int(input())):
    n = int(input())
    answer = []
    idx = i
    while n > 0:
        while n < dp[idx]:
            idx -= 1
        answer.append(dp[idx])
        n -= dp[idx]
    print(' '.join(str(num) for num in sorted(answer)))