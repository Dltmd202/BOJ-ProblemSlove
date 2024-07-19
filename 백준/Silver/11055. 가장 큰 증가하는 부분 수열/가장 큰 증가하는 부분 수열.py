if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    dp = [0] * (n + 1)
    dp[0] = data[0]

    for target in range(1, n):
        for j in range(target):
            if data[j] < data[target]:
                dp[target] = max(dp[j] + data[target], dp[target])
            else:
                dp[target] = max(data[target], dp[target])

    print(max(dp))
