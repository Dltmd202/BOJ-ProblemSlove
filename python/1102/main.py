from collections import defaultdict
import sys
input = sys.stdin.readline

INF = int(1e9)

dp = defaultdict(lambda: -1)

n = int(input())
full = ((1 << n) - 1)
graph = [list(map(int, input().split())) for _ in range(n)]
s = input()
p = int(input())
visit = 0

for char in range(len(s)):
    if s[char] == 'Y':
        visit |= (1 << char)

dp[visit] = 0
for i in range(1 << n):
    if dp[i] == -1:
        continue
    for j in range(n):
        if i & (1 << j):
            for k in range(n):
                if not i & (1 << k):
                    if dp[i | (1 << k)] == -1 or \
                            dp[i | (1 << k)] > dp[i] + graph[j][k]:
                        dp[i | (1 << k)] = dp[i] + graph[j][k]

ans = INF
for i in range(1 << n):
    if dp[i] == -1:
        continue
    cnt = 0
    for j in range(n):
        if i & (1 << j):
            cnt += 1
    if cnt >= p:
        if ans > dp[i]:
            ans = dp[i]
print(-1 if ans == INF else ans)