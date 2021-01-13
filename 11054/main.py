#11054
#https://www.acmicpc.net/problem/11054

n = int(input())

data = list(map(int,input().split()))


dp = [[1]*(2) for _ in range(n)]
ddp = [[1]*(2) for _ in range(n)]



max_value = 0
for i in range(1,n):
    for j in range(0,i):
        if data[i] > data[j]:
            max_value=max(max_value,dp[j][1]+1)
            dp[i][1] = max(dp[i][1],dp[j][1]+1)
        ddp[i][1] = max_value


max_value=0


for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if data[i] > data[j]:
            max_value=max(max_value,dp[j][0]+1)
            dp[i][0] = max(dp[i][0],dp[j][0]+1)
        ddp[i][0] = max_value



answer = 0
for i in range(len(dp)):
    buf = sum(dp[i])-1
    answer = max(buf,answer)
print(answer)