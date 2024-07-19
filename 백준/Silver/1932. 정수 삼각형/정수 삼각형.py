if __name__ == '__main__':
    n = int(input())
    data = [0]

    for i in range(n):
        data.extend(list(map(int, input().split())))

    dp = [-1] * len(data)


    def search(idx, depth):
        if idx >= len(data):
            return 0
        if dp[idx] != -1:
            return dp[idx]

        left_idx = idx + (depth + 1)
        right_idx = idx + (depth + 2)

        tmp = data[idx] + max(search(left_idx, depth + 1), search(right_idx, depth + 1))
        dp[idx] = tmp
        return tmp

    print(search(1, 0))
