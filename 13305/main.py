
n = int(input())

edges = list(map(int,input().split()))
price = list(map(int,input().split()))

dp = [0]*(n)

p = price[0]
dp[0]=p*edges[0]

for i in range(1,n-1):
    if p > price[i]:
        p = price[i]
    dp[i] = dp[i-1] +p * edges[i]
print(dp[-2])