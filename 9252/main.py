

first = [' '] + list(input().strip())
second = [' '] + list(input().strip())

graph = [[''] * (len(second) + 1) for _ in range(len(first) + 1)]
dp = [[''] * (len(second) + 1) for _ in range(len(first) + 1)]


for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            dp[i][j] = dp[i - 1][j - 1] + first[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]


print(len(dp[len(first) - 1][len(second) - 1]))
if len(dp[len(first) - 1][len(second) - 1]) > 0:
    print(dp[len(first) - 1][len(second) - 1])
