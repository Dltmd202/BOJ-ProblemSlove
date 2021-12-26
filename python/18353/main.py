#18353
#https://www.acmicpc.net/problem/18353

n = int(input())

data = list(map(int,input().split()))
dp = [1]*n

data.reverse()


for i in range(1,n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i],dp[j] + 1)
print(n - max(dp))