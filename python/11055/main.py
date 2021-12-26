from copy import deepcopy
n = map(int,input().split())
data = list(map(int,input().split()))




def solution(data):
    data = [0] + data
    dp = [-1] *(len(data))
    dp[-1]=data[-1]
    max_value = 0

    def sol(start):
        if dp[start] != -1:
            return dp[start]
        ret = data[start]
        for i in range(start+1,len(data)):
            if data[start] < data[i]:
                ret = max(ret , sol(i)+data[start])
        max_value = 0
        if ret == data[start]:
            max_value = max(dp[start:])
            max_value = max(max_value,ret)

        dp[start]=ret
        return ret
    sol(0)
    return dp
dp = solution(data)
print(max(dp))