import sys
input = sys.stdin.readline
MOD = 1_000_000_009

if __name__ == '__main__':
    n = int(input())
    data = [int(input()) for _ in range(n)]
    max_val = max(data)

    dp = [0] * (max_val + 4)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, max_val + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

    print('\n'.join(str(dp[d]) for d in data))

