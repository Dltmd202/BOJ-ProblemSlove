#9251
#https://www.acmicpc.net/problem/9251



a = input()
b = input()
a=' '+a
b=' '+b
dp =[[0]*(len(b)) for _ in range(len(a))]


for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])