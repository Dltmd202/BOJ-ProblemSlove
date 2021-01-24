import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n = int(input())

data =[]
maxvalue = 0
for i in range(n):
    x = int(input())
    maxvalue =max(maxvalue ,x)
    data.append(x)

def solution(data , maxvalue):
    dp = [0]*(maxvalue + 1)
    dp[1]=1
    dp[2]=2
    dp[3]=4
    if maxvalue <= 3:
        return dp

    for i in range(4,maxvalue+1):
        dp[i] = (dp[i-1] +  dp[i-2] + dp[i-3]) % 1000000009
    return dp

dp = solution(data,maxvalue)

for i in data:
    print(dp[i])




