N = 10_000

dp = [1] * (N + 1)

for i in range(2, N + 1):
    dp[i] += dp[i - 2]

for i in range(3, N + 1):
    dp[i] += dp[i - 3]

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        print(dp[int(input())])
