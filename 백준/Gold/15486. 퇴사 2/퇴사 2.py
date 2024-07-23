import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    t, p = [], []

    for i in range(n):
        tmp = list(map(int, input().split()))
        t.append(tmp[0] - 1)
        p.append(tmp[1])

    dp = [0] * n
    max_val = 0

    for i in range(n):
        try:
            dp[i] = max(dp[i - 1], dp[i])
            dp[i + t[i]] = max(dp[i + t[i]], dp[i - 1] + p[i])
        except:
            pass
    print(max(dp))
