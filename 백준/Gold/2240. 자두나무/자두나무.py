if __name__ == '__main__':
    t, w = map(int, input().split())
    fruits = [0] + [int(input()) for _ in range(t)]
    dp = [[0] * (w + 1) for _ in range(t + 1)]

    if fruits[1] == 1:
        dp[1][0] = 1
    else:
        dp[1][1] = 1

    for i in range(2, t + 1):
        for j in range(w + 1):
            tmp = 0
            if j % 2 == 0 and fruits[i] == 1:
                tmp = 1
            elif j % 2 == 1 and fruits[i] == 2:
                tmp = 1
            dp[i][j] = max(dp[i - 1][:j + 1]) + tmp

    print(max(dp[t]))
