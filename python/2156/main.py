#2156
#https://www.acmicpc.net/problem/2156

n = int(input())
data = [0]

for i in range(n):
    data.append(int(input()))

dp = [0]
dp.append(data[1])
if (n > 1):
    dp.append(data[1] + data[2])


for i in range(3, n + 1):
    first = data[i] + dp[i-2]
    second = data[i] + data[i-1] +dp[i-3]
    third = dp[i-1]
    m = max(first,second,third)
    dp.append(m)

print(dp[n])