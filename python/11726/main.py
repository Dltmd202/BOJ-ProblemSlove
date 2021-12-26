#11726
#Dynamic Programing
#O(N)

n = int(input())

def solution(n):

    dp = [0]*(n+3)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%10007
    return dp[n]

print(solution(n))