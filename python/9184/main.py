#9184
#https://www.acmicpc.net/problem/9184




graph = []

while True:
    a , b ,c = map(int,input().split())
    if a == -1 and b == -1 and c == - 1:
        break
    graph.append(([a,b,c]))


dp = [[[0]*(102) for _ in range(102) ]for _ in range(102)]


def index(idx):
    if idx < 0 :
        return 50 + idx
    else :
        return 51 + idx



for i in range(index(-50),index(51)):
    for j in range(index(-50),index(51)):
        for k in range(index(-50),index(51)):
            if i<= index(0) or j <= index(0) or k <= index(k) :
                dp[i][j][k] = 1




for i in range(index(1),index(21)):
    for j in range(index(1),index(21)):
        for k in range(index(1),index(21)):
            if ( i < j and j < k):
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else :
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

for i in range(index(1),index(51)):
    for j in range(index(1),index(51)):
        for k in range(index(1),index(51)):
            if i > index(20) or j > index(20) or k > index(20):
                dp[i][j][k] = dp[index(20)][index(20)][index(20)]



for i in graph:
    a,b,c = i
    print("w(%d, %d, %d) ="%(a,b,c),dp[index(a)][index(b)][index(c)])