import math

n = int(input())

data = []

for i in range(n):
    a,b = map(int,input().split())
    data.append((a,b))

def solution(data):
    data = [(1,0)] + data
    dp=[-1]*(len(data))

    def sol(start):
        if dp[start] != -1:
            return dp[start]
        if data[start][0]+start > len(data):
            dp[start] = 0
            return dp[start]

        ret =  data[start][1]
        cost = ret

        for i in range(start + data[start][0] ,len(data)):
            cost = max(cost , sol(i)+ret)
        dp[start] = cost
        return dp[start]
    sol(0)
    return max(dp)

print(solution(data))

