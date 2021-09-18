n = int(input())

data = []

for i in range(n):
    a ,b = map(int,input().split())
    data.append((a,b))

data.sort(key=lambda x:[x[0],x[1]])

dp = [1]*(n+1)

for i in range(1,n):
    for j in range(0,i):
        if data[i][1] > data[j][1]:
            dp[i]= max(dp[i],dp[j]+1)

print(n-max(dp))