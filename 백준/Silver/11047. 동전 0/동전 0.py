if __name__ == '__main__':
    n, k = map(int, input().split())
    coins = list(map(int, [input() for _ in range(n)]))
    coins.sort(reverse=True)

    answer = 0
    for coin in coins:
        answer += k // coin
        k %= coin

    print(answer)