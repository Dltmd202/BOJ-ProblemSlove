if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        N = int(input())
        data = list(map(int, input().split()))

        money = 0
        max_price = 0
        for i in range(len(data) - 1, -1, -1):
            if data[i] > max_price:
                max_price = data[i]
            else:
                money += max_price - data[i]
        print(money)