import sys
from copy import deepcopy
input = sys.stdin.readline
N = int(input())
table = list(map(int, input().split()))
max_dp = deepcopy(table)
min_dp = deepcopy(table)
for i in range(1, N):
    table = list(map(int, input().split()))
    max_dp[0], max_dp[1], max_dp[2] = table[0] + max(max_dp[0: 2]), \
                                      table[1] + max(max_dp[0: 3]), table[2] + max(max_dp[1: 3])
    min_dp[0], min_dp[1], min_dp[2] = table[0] + min(min_dp[0: 2]), \
                                      table[1] + min(min_dp[0: 3]), table[2] + min(min_dp[1: 3])

print(max(max_dp), min(min_dp))

