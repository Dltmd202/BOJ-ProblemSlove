

n =int(input())
data = list(map(int,input().split()))
dp = [int(-1e9)]*(n+1)
dp[0]=data[0]
sum = 0
for i in range(1,n):
    dp[i]= max(dp[i-1]+data[i],data[i])
print(max(dp))


