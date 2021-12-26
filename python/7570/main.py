
n = int(input())
data = list(map(int, input().split()))
dp = [0] * (n + 1)
long = 0

for i in range(n):
    idx = data[i]
    dp[idx] = dp[idx - 1] + 1
    long = max(dp[idx], dp[idx - 1] + 1)
print(n - max(dp))