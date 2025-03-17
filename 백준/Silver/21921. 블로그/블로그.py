if __name__ == '__main__':
    n, x = map(int, input().split())
    data = list(map(int, input().split()))
    prefix_sum = [0]
    max_sum = 0
    count = 0

    for d in data:
        prefix_sum.append(prefix_sum[-1] + d)

    tmp = 0
    for i in range(x, n + 1):
        tmp = prefix_sum[i] - prefix_sum[i - x]

        if tmp > max_sum:
            max_sum = tmp
            count = 1
        elif max_sum == tmp:
            count += 1

    if max_sum != 0:
        print(max_sum)
        print(count)
    else:
        print('SAD')