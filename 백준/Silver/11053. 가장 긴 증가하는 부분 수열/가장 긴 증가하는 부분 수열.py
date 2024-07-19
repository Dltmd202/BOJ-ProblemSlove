import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    dp = [1] * n

    for target in range(1, n):
        for j in range(target):
            if data[target] > data[j]:
                dp[target] = max(dp[target], dp[j] + 1)

    print(max(dp))
