if __name__ == '__main__':
    a = int(input())
    data = list(map(int, input().split()))

    dp = [1] * a

    for target in range(1, a):
        for j in range(target):
            if data[target] > data[j]:
                dp[target] = max(dp[target], dp[j] + 1)

    x = max(dp)
    print(x)

    result = []
    for i in range(a - 1, -1, -1):
        if x == dp[i]:
            result.append(str(data[i]))
            x -= 1
    print(' '.join(reversed(result)))
